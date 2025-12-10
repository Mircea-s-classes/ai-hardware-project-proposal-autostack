# University of Virginia
## Department of Electrical and Computer Engineering

**Course:** ECE 4332 / ECE 6332 — AI Hardware Design and Implementation  
**Semester:** Fall 2025  
**Proposal Deadline:** November 5, 2025 — 11:59 PM  
**Submission:** Upload to Canvas (PDF) and to GitHub (`/docs` folder)

---

# AI Hardware Project Proposal

## 1. Project Title
Autostack

Frank Wu, Tony Xu, Anson Lu, Yingming Ma

## 2. Platform Selection
Platform: Raspberry Pi 5 (maybe with AI Kit as well)

This project builds on our ECE Capstone work: an automated alignment system designed for use under a telescope. Since the system already utilizes a Raspberry Pi 5 for motor control, implementing our AI-based detection system on the same platform would be both efficient and practical.

**Undergraduates:** Edge-AI, TinyML

## 3. Problem Definition
We will design an AI algorithmn that detects small metal plate on a substrate with image input from integrated camera on microscope. The algorithmn will run on Raspberry PI and guide the motor to align the two metal plates. It will help researchers using microscope to align the sample more easily.

## 4. Technical Objectives
1. Detect flake candidates in the image, estimate their areas, and automatically select the flake with the largest area as the target.
2. Verify that the motorized stage moves by the commanded distance. If the observed displacement deviates from the command, automatically apply corrective motion to eliminate positioning error.
3. Detect the color shift that occurs when two flakes successfully make contact. Use this signal as feedback to adjust Z-axis pressure in real time and ensure reliable stacking.

## 5. Methodology
Our approach will build upon the existing hardware from our ECE Capstone project, integrating new software capabilities for automated visual detection and alignment. The hardware platform is centered on a Raspberry Pi 5, which already serves as the motor control unit in our current system. This allows for seamless integration of the proposed AI-based detection functionality within the same embedded environment.

The software development will primarily utilize Python, the native programming language supported by the Raspberry Pi. Established deep learning frameworks such as Keras and PyTorch will be employed to facilitate model training and inference. The implementation will proceed in two stages:

1. Baseline Detection: We will first implement a traditional edge detection algorithm (e.g., Canny or Sobel) to identify object boundaries without relying on machine learning.

2. AI-Based Detection: We will then compare the baseline results to those obtained using machine learning–based object detection models, such as YOLO and R-CNN, to evaluate performance improvements in accuracy and robustness.

For validation, we will estimate the detected metal flake dimensions based on captured images and compare them to visual (eyeballed) measurements. Further validation will be achieved by assessing the accuracy of flake positioning and alignment after automated transformation between target locations.

## 6. Expected Deliverables
We will provide a working demo of computer vision incorporated into the microscope image analysis. The analyzed result will be used in moter control operations. The training code will be provided in github repo. At the end of semester we will present with a working demo alongside presentation slides. Final report will be delivered if required.

## 7. Team Responsibilities

| Name | Role | Responsibilities |
|------|------|------------------|
| Frank Wu | Team Lead | Coordination, documentation |
| Tony Xu | Hardware | Setup, integration |
| Anson Lu | Software | Model training, inference |
| Yingming Ma | Evaluation | Testing, benchmarking |

## 8. Timeline and Milestones
Provide expected milestones: DataSet Found, Edge Detection Finished, AI-Based Detection Finished, Motor Movement Detection Added, Color Shift Algorithm Added


| Week | Milestone | Deliverable |
|------|------------|-------------|
| 2 | Proposal | PDF + GitHub submission |
| 3 | Find DataSet | A collection of images |
| 4 | Flake Detection Propotype Finished | A working Propotype with low accueacy |
| 4 | Midterm presentation | Slides, preliminary results |
| 5 | Technical Objective 2,3 added | Demo of working algorithm |
| 6 | Integration & testing | Working prototype |
| Dec. 18 | Final presentation | Report, demo, GitHub archive |

## 9. Resources Required
Most of the required hardware components will be provided through our existing ECE Capstone project setup. Additional hardware, such as an AI development kit or camera module, may be needed to support on-device model inference and image acquisition.

For AI model training, we will require a dataset of metal flake images captured under a telescope. This dataset will serve as the foundation for both traditional image processing and machine learning–based detection methods, enabling model development, testing, and validation.

## 10. References
Yolo:  [1] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You Only Look Once: Unified, Real-Time Object Detection,” May 09, 2016, arXiv: arXiv:1506.02640. doi: 10.48550/arXiv.1506.02640.

R-CNN: [2] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks,” Jan. 06, 2016, arXiv: arXiv:1506.01497. doi: 10.48550/arXiv.1506.01497.

