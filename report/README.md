# Report
Include your final report (PDF, DOCX, and LaTeX files).
## HowTo: Run YOLO Inference on Raspberry Pi

This section explains how to run the trained YOLO model on a Raspberry Pi using the provided inference script and observe hardware performance metrics such as inference time and CPU utilization.

The script used for inference is:
yolo_run.py

### 1. Clone the Repository on the Raspberry Pi

Open a terminal on the Raspberry Pi and run:

```bash
git clone https://github.com/Mircea-s-classes/ai-hardware-project-proposal-autostack.git
cd ai-hardware-project-proposal-autostack

2. Run YOLO Inference
From the project root directory, run:

python yolo_run.py

This script performs the following actions:

Loads a trained YOLO model (best.pt)

Runs inference on an input image

Measures inference execution time

Measures average CPU usage

Measures peak CPU usage

Saves the detection output image

3. Console Output
When executed, the script prints output similar to:

Running YOLO inference with CPU monitoring...
Inference time: X.XXX seconds
Average CPU usage during inference: YY.Y%
Peak CPU usage during inference: ZZ.Z%

These values are used to evaluate embedded hardware performance on the Raspberry Pi.

4. Where Results Are Stored
The YOLO prediction output image is saved to:

report/YOLO_Output/
This directory contains the input image with bounding boxes drawn, along with YOLO inference result files.

5. Customizing Inference Inputs and Models
The paths used in yolo_run.py can be modified to test different images or models.

To change the input image, edit the following line in yolo_run.py:

source="../validation_dataset/images/r9.jpg"
Sample images for inference are provided in:

src/model/yolo_project/validation_dataset/
Any image in this directory (or a custom image path) can be used for inference.

To change the model used for inference, edit the model loading line in yolo_run.py:

model = YOLO("src/model/yolo_project/runs/detect/<run_name>/weights/best.pt")
Different trained models can be found in:

src/model/yolo_project/runs/detect/
Example model folders include:

flakes_yolov8n_640

flakes_yolov8n_1024

flakes_yolov8s_640

flakes_yolov8s_1024

Each folder contains a weights/best.pt file that can be selected for inference.

