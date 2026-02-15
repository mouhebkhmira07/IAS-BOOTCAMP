from ultralytics import YOLO

# Load pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train on laser detection dataset
model.train(
    data="Laser-detection-1/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="laser-leak-detector",
    project="runs"
)

# Evaluate
metrics = model.val()
print(f"mAP50: {metrics.box.map50:.4f}")
print(f"mAP50-95: {metrics.box.map:.4f}")
