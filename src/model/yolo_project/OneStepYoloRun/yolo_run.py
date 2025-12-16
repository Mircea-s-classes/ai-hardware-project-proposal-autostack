# from ultralytics import YOLO
# 
# model = YOLO("/home/autostack/Documents/AI_Hardware/ai-hardware-project-proposal-autostack/src/model/yolo_project/runs/detect/train/weights/best.pt")
# 
# model.predict(source= "../validation_dataset/images/r9.jpg", project = "/home/autostack/Documents/AI_Hardware/ai-hardware-project-proposal-autostack/report/", name="YOLO_Output", save = True, exist_ok=True)
from ultralytics import YOLO
import time
import psutil
import threading

# Load your trained model
model = YOLO("/home/autostack/Documents/AI_Hardware/ai-hardware-project-proposal-autostack/src/model/yolo_project/runs/detect/flakes_yolov8s_1024/weights/best.pt")

cpu_samples = []
monitor_running = True

def monitor_cpu():
    """Continuously sample CPU usage while YOLO is running."""
    global monitor_running
    while monitor_running:
        cpu_samples.append(psutil.cpu_percent(interval=0.2))

# Start CPU monitor thread
monitor_thread = threading.Thread(target=monitor_cpu, daemon=True)
monitor_thread.start()

print("Running YOLO inference with CPU monitoring...")

# Time inference
t0 = time.perf_counter()

results = model.predict(
    source="../validation_dataset/images/r9.jpg",
    project="/home/autostack/Documents/AI_Hardware/ai-hardware-project-proposal-autostack/report/",
    name="YOLO_Output",
    save=True,
    exist_ok=True,
)

t1 = time.perf_counter()
monitor_running = False
monitor_thread.join()

# Compute stats
elapsed = t1 - t0
avg_cpu = sum(cpu_samples) / len(cpu_samples)
max_cpu = max(cpu_samples)

print(f"Inference time: {elapsed:.3f} seconds")
print(f"Average CPU usage during inference: {avg_cpu:.1f}%")
print(f"Peak CPU usage during inference: {max_cpu:.1f}%")
