import cv2
from ultralytics import YOLO
from preprocess import preprocess_for_yolo  

# Load pretrained YOLOv8n
model = YOLO("yolov8n.pt")

# Path to a single image you want to test
img_path = "synthetic_flakes/images/0000.png"

# Read image
img = cv2.imread(img_path)

# Preprocess it
preprocessed = preprocess_for_yolo(img)

# Run YOLO inference
results = model(preprocessed)

# Show results in a window (with bounding boxes)
results[0].show()

# Optional: save the result to disk
save_path = "testresult_forone/yolo_test.png"
cv2.imwrite(save_path, results[0].plot())
print(f"Saved YOLO result to {save_path}")
