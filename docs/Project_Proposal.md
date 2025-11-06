# University of Virginia
## Department of Electrical and Computer Engineering

**Course:** ECE 4332 / ECE 6332 — AI Hardware Design and Implementation  
**Semester:** Fall 2025  
**Proposal Deadline:** November 5, 2025 — 11:59 PM  
**Submission:** Upload to Canvas (PDF) and to GitHub (`/docs` folder)

---

# AI Hardware Project Proposal Template

## 1. Project Title
Autostack

Frank Wu, Tony Xu, Anson Lu, Yingming Ma

## 2. Platform Selection
Platform: Raspberry Pi 5 (maybe with AI Kit as well)

This project builds on our ECE Capstone work: an automated alignment system designed for use under a telescope. Since the system already utilizes a Raspberry Pi 5 for motor control, implementing our AI-based detection system on the same platform would be both efficient and practical.

**Undergraduates:** Edge-AI, TinyML, or Neuromorphic platforms  
**Graduates:** open-source AI accelerators (Ztachip, VTA, Gemmini, VeriGOOD-ML, NVDLA) or any of the above 

## 3. Problem Definition
We will design an AI algorithmn that detects small metal plate on a substrate with image input from integrated camera on microscope. The algorithmn will run on Raspberry PI and guide the motor to align the two metal plates. It will help researchers using microscope could align the sample more easily.

Describe the AI or hardware design problem you aim to address and its relevance to AI hardware (e.g., efficiency, latency, scalability).

## 4. Technical Objectives
1. Detect flake candidates in the image, estimate their areas, and automatically select the flake with the largest area as the target.
2. Verify that the motorized stage moves by the commanded distance. If the observed displacement deviates from the command, automatically apply corrective motion to eliminate positioning error.
3. Detect the color shift that occurs when two flakes successfully make contact. Use this signal as feedback to adjust Z-axis pressure in real time and ensure reliable stacking.

## 5. Methodology
Describe your planned approach: hardware setup, software tools, model design, performance metrics, and validation strategy.

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
Provide expected milestones:

| Week | Milestone | Deliverable |
|------|------------|-------------|
| 2 | Proposal | PDF + GitHub submission |
| 4 | Midterm presentation | Slides, preliminary results |
| 6 | Integration & testing | Working prototype |
| Dec. 18 | Final presentation | Report, demo, GitHub archive |

## 9. Resources Required
List special hardware, datasets, or compute access needed.

## 10. References
Include relevant papers, repositories, and documentation.
