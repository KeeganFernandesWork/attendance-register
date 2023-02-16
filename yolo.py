from ultralytics import YOLO
import numpy as np
model = YOLO("best_attendance.pt")
def model_yolo(image = "hello.jpg"):
    results = model(image)
    labels = {0:"Rahil",1:"Keegan"}
    classes = []

    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        for box in boxes:
            label = int(box.cls.cpu().numpy())
            classes.append([labels[label], float(box.conf.cpu().numpy())])
    print(classes)
    return classes

