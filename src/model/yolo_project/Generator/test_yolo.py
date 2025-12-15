from ultralytics import YOLO

# Load the small YOLOv8n model
model = YOLO("yolov8n.pt")

# Run inference on an example image
results = model("https://ultralytics.com/images/bus.jpg")

# Show the result (opens a window with bounding boxes)
results[0].show()
