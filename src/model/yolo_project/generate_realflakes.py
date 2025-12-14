import cv2
import numpy as np
import os
import random

OUTPUT_DIR = "synthetic_flakes"
IMG_SIZE = 640
NUM_IMAGES = 500     # adjust as you like

os.makedirs(f"{OUTPUT_DIR}/images", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/labels", exist_ok=True)

def make_irregular_polygon(center, scale):
    """Generate irregular polygon for flake."""
    num_points = random.randint(5, 12)
    angles = np.sort(np.random.rand(num_points) * 2 * np.pi)
    radius = scale * (0.5 + np.random.rand(num_points) * 0.5)

    pts = np.vstack([
        center[0] + radius * np.cos(angles),
        center[1] + radius * np.sin(angles)
    ]).T

    return pts.astype(np.int32)

def add_microscope_background(img):
    """
    Simulate microscope uneven lighting with subtle gradient:
    - Combine horizontal + vertical gradient
    - Optional soft random spots (blurred for smoothness)
    """
    h, w, _ = img.shape
    
    # Base gradient
    grad_x = np.linspace(0, random.randint(30, 70), w, dtype=np.float32)
    grad_x = np.tile(grad_x, (h, 1))
    
    grad_y = np.linspace(0, random.randint(20, 50), h, dtype=np.float32)
    grad_y = np.tile(grad_y, (w, 1)).T
    
    gradient = grad_x + grad_y

    # Optional subtle spots
    spots = np.zeros((h, w), dtype=np.float32)
    for _ in range(random.randint(2, 4)):
        radius = random.randint(50, 120)
        center = (random.randint(0, w-1), random.randint(0, h-1))
        intensity = random.uniform(-20, 20)  # small intensity
        cv2.circle(spots, center, radius, intensity, -1)
    
    # Blur spots to make smooth illumination
    spots = cv2.GaussianBlur(spots, (101, 101), 0)
    
    # Combine gradient + spots
    gradient += spots

    # Clip and convert to uint8
    gradient = np.clip(gradient, 0, 255).astype(np.uint8)
    gradient_3ch = cv2.merge([gradient, gradient, gradient])
    
    # Add to image
    img = cv2.add(img, gradient_3ch)
    
    return img

def random_flake_color():
    """Return a realistic random flake color."""
    # colors tend to be pale/bright, similar to real flakes
    return tuple(np.random.randint(100, 255, size=3).tolist())

for i in range(NUM_IMAGES):
    # Base background
    base = random.randint(180, 230)
    img = np.ones((IMG_SIZE, IMG_SIZE, 3), dtype=np.uint8) * base

    img = add_microscope_background(img)

    mask = np.zeros((IMG_SIZE, IMG_SIZE), dtype=np.uint8)
    bboxes = []

    num_flakes = random.randint(1, 4)

    for _ in range(num_flakes):
        # Random center and size
        cx = random.randint(80, IMG_SIZE-80)
        cy = random.randint(80, IMG_SIZE-80)
        size = random.randint(30, 120)

        poly = make_irregular_polygon((cx, cy), size)

        # Random color
        color = random_flake_color()
        cv2.fillPoly(img, [poly], color)

        # Draw mask for bbox calculation
        cv2.fillPoly(mask, [poly], 255)

        # Get bounding box
        xs = poly[:, 0]
        ys = poly[:, 1]
        x1, y1 = xs.min(), ys.min()
        x2, y2 = xs.max(), ys.max()

        # YOLO format
        yolo_cx = (x1 + x2) / 2 / IMG_SIZE
        yolo_cy = (y1 + y2) / 2 / IMG_SIZE
        yolo_w  = (x2 - x1) / IMG_SIZE
        yolo_h  = (y2 - y1) / IMG_SIZE

        bboxes.append((0, yolo_cx, yolo_cy, yolo_w, yolo_h))

    # Apply contrast reduction on flake (mimic real contrast)
    flake_region = mask > 0
    img[flake_region] = np.clip(img[flake_region] - random.randint(10, 45), 0, 255)

    # Add gaussian noise
    noise = np.random.normal(0, 3, img.shape).astype(np.int16)
    img = np.clip(img + noise, 0, 255).astype(np.uint8)

    # Apply slight blur to mimic microscope focus
    ksize = random.choice([3,5,7])
    img = cv2.GaussianBlur(img, (ksize, ksize), 0)

    cv2.imwrite(f"{OUTPUT_DIR}/images/{i:04d}.png", img)

    # Save labels
    with open(f"{OUTPUT_DIR}/labels/{i:04d}.txt", "w") as f:
        for bbox in bboxes:
            cls, x, y, w, h = bbox
            f.write(f"{cls} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")

    print(f"Generated image {i+1}/{NUM_IMAGES}")

print("Done — synthetic microscope flakes created!")
