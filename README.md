# 🔦 Laser Leak Detection System

This project is a computer vision-based system designed to detect air leakage in industrial pipes. 
It operates on the principle of **laser signature loss**: if a laser beam directed along a pipe is missing or fragmented, it indicates a disturbance likely caused by high-pressure air leakage.

## Features
- Real-time image analysis using YOLOv8 via Roboflow.
- Automated leak alerts when laser signatures are missing.
- Interactive Streamlit dashboard for easy operator use.

## Installation

1. Clone or copy the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

```bash
streamlit run app.py
```

## How it Works
1. Upload an image or provide a video stream of the pipe under inspection.
2. The system triggers the Roboflow model to detect the laser line.
3. If the laser is detected, the status remains "Safe".
4. If no laser is found or the detection confidence is low, the system triggers a **"Leak Detected"** alert.

---
*Built for the IAS Bootcamp Challenge.*
