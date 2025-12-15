import cv2
import glob
import os
from ultralytics import YOLO
from preprocess import preprocess_for_yolo  # your preprocessing function

# Load pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Paths
IMG_DIR = "synthetic_flakes/images"         # folder with your 500 images
OUTPUT_DIR = "testresult_forall"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop through all images
for img_path in glob.glob(f"{IMG_DIR}/*.png"):
    # Read image
    img = cv2.imread(img_path)
    
    # Apply preprocessing
    preprocessed = preprocess_for_yolo(img)
    
    # Run YOLO inference
    results = model(preprocessed)
    
    # Keep original filename
    filename = os.path.basename(img_path)  # e.g., "0000.png"
    save_path = os.path.join(OUTPUT_DIR, filename)
    
    # Save result image with bounding boxes
    cv2.imwrite(save_path, results[0].plot())
    
    print(f"Processed {filename} → saved to {save_path}")

print("All images processed!")
