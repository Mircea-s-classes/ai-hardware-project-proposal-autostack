[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/v3c0XywZ)
# AI Hardware Project Template
ECE 4332 / ECE 6332 — AI Hardware  
Fall 2025

## 🧭 Overview
This repository provides a structured template for your team project in the AI Hardware class.  
Each team will **clone this template** to start their own project repository.

## 🗂 Folder Structure
- `docs/` – project proposal and documentation  
- `presentations/` – midterm and final presentation slides  
- `report/` – final written report (IEEE LaTeX and DOCX versions included)  
- `src/` – source code for software, hardware, and experiments  
- `data/` – datasets or pointers to data used

## 🧑‍🤝‍🧑 Team Setup
Each team should have **2–4 members (3 preferred)**.  
List all team members in `docs/Project_Proposal.md`.

## 📋 Required Deliverables
1. **Project Proposal** — due Nov. 5, 2025, 11:59 PM  
2. **Midterm Presentation** — Nov. 19,2025, 11:59 PM  
3. **Final Presentation and Report** — Dec. 17, 11:59 PM

## 🚀 How to Use This Template
1. Click **“Use this template”** on GitHub.  
2. Name your repo `ai-hardware-teamXX` (replace XX with your team name or number).  
3. Clone it locally:
   ```bash
   git clone https://github.com/YOUR-ORG/ai-hardware-teamXX.git
   ```
4. Add your work in the appropriate folders.

## 🧾 Submissions
- Commit and push all deliverables before each deadline.
- Tag final submissions with:
   ```bash
   git tag v1.0-final
   git push origin v1.0-final
   ```

## 📜 License
This project is released under the MIT License.

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
