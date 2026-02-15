import os
os.environ["MLFLOW_TRACKING_URI"] = ""  # Disable MLflow to avoid registry error
os.environ["WANDB_DISABLED"] = "true"
from ultralytics import YOLO

ROOT = os.path.dirname(os.path.abspath(__file__))

model = YOLO("yolov8n.pt")

model.train(
    data=os.path.join(ROOT, "Laser-detection-1", "data.yaml"),
    epochs=50,
    imgsz=640,
    batch=16,
    name="laser-leak-detector",
    project=os.path.join(ROOT, "runs"),
    exist_ok=True
)

metrics = model.val()
print(f"\nmAP50: {metrics.box.map50:.4f}")
print(f"mAP50-95: {metrics.box.map:.4f}")
