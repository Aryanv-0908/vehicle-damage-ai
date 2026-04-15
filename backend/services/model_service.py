from ultralytics import YOLO
model = YOLO("yolov8n.pt")

def run_detection(image_path):
    results = model(image_path)

    detections = []

    for r in results:
        for box in r.boxes:
            detections.append({
                "class": int(box.cls),
                "confidence": float(box.conf)
            })

    return detections