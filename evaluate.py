import os
from ultralytics import YOLO

ROOT = os.path.dirname(os.path.abspath(__file__))
BEST_MODEL = os.path.join(ROOT, "runs", "laser-leak-detector", "weights", "best.pt")

if not os.path.exists(BEST_MODEL):
    print(f"❌ Model not found at {BEST_MODEL}")
    print("   Run 'python train.py' first and WAIT for it to finish.")
    exit(1)

model = YOLO(BEST_MODEL)

metrics = model.val(
    data=os.path.join(ROOT, "Laser-detection-1", "data.yaml"),
    plots=True,
    project=os.path.join(ROOT, "runs"),
    name="evaluation",
    exist_ok=True
)

print("\n" + "=" * 50)
print("📊 RAPPORT D'ÉVALUATION")
print("=" * 50)
print(f"  Précision:    {metrics.box.mp:.4f}")
print(f"  Rappel:       {metrics.box.mr:.4f}")
print(f"  mAP@50:       {metrics.box.map50:.4f}")
print(f"  mAP@50-95:    {metrics.box.map:.4f}")
f1 = 2 * metrics.box.mp * metrics.box.mr / (metrics.box.mp + metrics.box.mr + 1e-8)
print(f"  F1-Score:     {f1:.4f}")
print("=" * 50)

print(f"\n📁 Plots sauvegardés dans: {os.path.join(ROOT, 'runs', 'evaluation')}/")
print(f"   - confusion_matrix.png")
print(f"   - confusion_matrix_normalized.png")
print(f"   - P_curve.png / R_curve.png / PR_curve.png / F1_curve.png")
