from ultralytics import YOLO

model = YOLO("/home/autostack/Documents/AI_Hardware/ai-hardware-project-proposal-autostack/src/model/yolo_project/runs/detect/train/weights/best.pt")

model.predict(source= "../validation_dataset/images/r9.jpg", project = "/home/autostack/Documents/AI_Hardware/ai-hardware-project-proposal-autostack/report/", name="YOLO_Output", save = True, exist_ok=True)