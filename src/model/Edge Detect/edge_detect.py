import cv2 as cv
import numpy as np

# ============================
# Parameters
# ============================
IMAGE_PATH = "r9.jpg"

# Minimum area in pixels^2 to keep a flake (tune this!)
MIN_AREA = 200.0   # ignore tiny dust/noise

# ============================
# 1. Load image and preprocess
# ============================
img = cv.imread(IMAGE_PATH)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Strong blur to suppress gradual color changes
blur = cv.GaussianBlur(gray, (11, 11), 0)

# Canny (sharp edges only)
edges = cv.Canny(
    blur,
    threshold1=30,
    threshold2=50
)

# ============================
# 2. Connect edges into closed regions
# ============================
kernel = np.ones((5, 5), np.uint8)

edges_dilated = cv.dilate(edges, kernel, iterations=1)
closed = cv.morphologyEx(edges_dilated, cv.MORPH_CLOSE, kernel, iterations=2)

# ============================
# 3. Find ALL outer contours (all flakes)
# ============================
contours, _ = cv.findContours(
    closed,
    cv.RETR_EXTERNAL,          # each connected region = one flake
    cv.CHAIN_APPROX_SIMPLE
)

print(f"Total contours found: {len(contours)}")

if len(contours) == 0:
    print("No flake-like region detected.")
    cv.imshow("Original", img)
    cv.imshow("Canny Edges", edges)
    cv.imshow("Closed", closed)
    cv.waitKey(0)
    cv.destroyAllWindows()
    raise SystemExit

# ============================
# 4. Create a filled mask (all flakes) and per-contour info
# ============================
mask_all = np.zeros_like(gray)
overlay = img.copy()

flake_info_contours = []  # list of (index, area, contour)

for i, cnt in enumerate(contours):
    area = cv.contourArea(cnt)
    if area < MIN_AREA:
        continue  # skip tiny noise

    flake_info_contours.append((i, area, cnt))

    # Fill this flake in the mask
    cv.drawContours(mask_all, [cnt], -1, 255, cv.FILLED)

# Draw all kept flakes on overlay (green fill, red border)
overlay[mask_all == 255] = (0, 255, 0)
for _, _, cnt in flake_info_contours:
    cv.drawContours(overlay, [cnt], -1, (0, 0, 255), 1)

# Sort flakes by area (largest first) – from contour-based step
flake_info_contours.sort(key=lambda x: x[1], reverse=True)

print("\nDetected flakes from contours (filtered by MIN_AREA):")
for rank, (idx, area, _) in enumerate(flake_info_contours, start=1):
    print(f"  Flake #{rank}: contour index={idx}, area={area:.2f} pixels^2")

# ============================
# 5. Connected components on the filled mask
#    (treat each white blob as a flake)
# ============================
_, mask_bin = cv.threshold(mask_all, 127, 255, cv.THRESH_BINARY)

num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(mask_bin)
# stats: [x, y, w, h, area]

flakes_cc = []
for label in range(1, num_labels):   # skip background (0)
    x, y, w, h, area = stats[label]
    if area < MIN_AREA:
        continue
    cx, cy = centroids[label]
    flakes_cc.append({
        "label": label,
        "area": area,
        "bbox": (x, y, w, h),
        "centroid": (cx, cy),
    })

# Sort by area (largest first)
flakes_cc.sort(key=lambda f: f["area"], reverse=True)

print("\nConnected-component flakes (after MIN_AREA):")
for i, f in enumerate(flakes_cc, start=1):
    print(f"  Flake #{i}: label={f['label']}, area={f['area']:.2f}, centroid={f['centroid']}")

# ============================
# 6. Color visualization + main (largest) flake mask
# ============================
h, w = mask_bin.shape
color_vis = np.zeros((h, w, 3), dtype=np.uint8)

for f in flakes_cc:
    label = f["label"]
    color = np.random.randint(0, 255, size=3).tolist()
    color_vis[labels == label] = color

if flakes_cc:
    # choose largest flake by area
    main_flake = flakes_cc[0]
    main_label = main_flake["label"]

    main_mask = np.zeros_like(mask_bin)
    main_mask[labels == main_label] = 255

    print(f"\nMain flake (largest) label={main_label}, area={main_flake['area']:.2f} pixels^2")
else:
    main_mask = np.zeros_like(mask_bin)
    print("\nNo flakes passed MIN_AREA in connected-components stage")

# ============================
# 7. Visualize results
# ============================
# cv.imshow("Original", img)
# cv.imshow("Blurred Gray", blur)
# cv.imshow("Canny Edges", edges)
# cv.imshow("Closed (for contours)", closed)
# cv.imshow("All Flakes Mask (Filled)", mask_all)
# cv.imshow("Overlay (All Flakes from Contours)", overlay)
# cv.imshow("Connected Components (colored flakes)", color_vis)
# cv.imshow("Main Flake (largest from CC)", main_mask)

# cv.waitKey(0)
# cv.destroyAllWindows()

# ============================
# 6. Draw bounding boxes + centroid for EVERY flake
# ============================
boxed_all = img.copy()

for i, f in enumerate(flakes_cc, start=1):
    label = f["label"]
    area = f["area"]
    (x, y, w, h) = f["bbox"]
    (cx, cy) = f["centroid"]
    cx, cy = int(cx), int(cy)

    # Bounding box (red)
    cv.rectangle(boxed_all, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Centroid (blue)
    cv.circle(boxed_all, (cx, cy), 4, (255, 0, 0), -1)

    # Label number near the centroid (white text)
    cv.putText(boxed_all, f"{i}", (cx + 5, cy - 5),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

print("\nBounding boxes + centroids drawn for all flakes.")

cv.imshow("Flake Locations (all flakes)", boxed_all)

cv.waitKey(0)
cv.destroyAllWindows()
