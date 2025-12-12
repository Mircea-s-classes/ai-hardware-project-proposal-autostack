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
    """Simulate microscope uneven lighting with a 3-channel gradient."""
    # 1D gradient from 0 to some max brightness
    grad_1d = np.linspace(0, random.randint(10, 40), IMG_SIZE, dtype=np.uint8)
    # Make it 2D: H x W
    gradient = np.tile(grad_1d, (IMG_SIZE, 1))
    # Make it 3-channel: H x W x 3
    gradient_3ch = cv2.merge([gradient, gradient, gradient])
    # Add to the image
    img = cv2.add(img, gradient_3ch)
    return img


for i in range(NUM_IMAGES):
    # Base background
    base = random.randint(180, 230)
    img = np.ones((IMG_SIZE, IMG_SIZE, 3), dtype=np.uint8) * base

    img = add_microscope_background(img)

    mask = np.zeros((IMG_SIZE, IMG_SIZE), dtype=np.uint8)
    bboxes = []

    num_flakes = random.randint(1, 4)

    for _ in range(num_flakes):
        # Random center
        cx = random.randint(80, IMG_SIZE-80)
        cy = random.randint(80, IMG_SIZE-80)
        size = random.randint(30, 120)

        poly = make_irregular_polygon((cx, cy), size)

        # Draw mask
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
    img[flake_region] -= random.randint(10, 45)

    # Add gaussian noise
    noise = np.random.normal(0, 3, img.shape).astype(np.int16)
    img = np.clip(img + noise, 0, 255).astype(np.uint8)

    cv2.imwrite(f"{OUTPUT_DIR}/images/{i:04d}.png", img)

    # Save labels
    with open(f"{OUTPUT_DIR}/labels/{i:04d}.txt", "w") as f:
        for bbox in bboxes:
            cls, x, y, w, h = bbox
            f.write(f"{cls} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")

    print(f"Generated image {i+1}/{NUM_IMAGES}")

print("Done — synthetic microscope flakes created!")
