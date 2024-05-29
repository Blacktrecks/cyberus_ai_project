import cv2
from config import *
from .camera import initCamera
from ..config import CONF_THRESHOLD, SIZE_THRESHOLD, SIZE_TOLERANCE

cap, model, classLabels, font, font_scale = initCamera()

def getObjectPos(objectName):
    """
    Detect the specified object in the video frame and return its position and size.
    
    :param objectName: Name of the object to detect.
    :return: (x, y) position of the object
    center, area of the bounding box.
    """
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to capture image from camera.")

    classIndex, confidence, bbox = model.detect(frame, confThreshold=CONF_THRESHOLD)
    object_name = None
    current_area = 0

    if len(classIndex) != 0:
        for class_ix, conf, boxes in zip(classIndex.flatten(), confidence.flatten(), bbox):
            if class_ix <= 80:  # Filter classes within COCO dataset range
                cv2.rectangle(frame, boxes, (225, 0, 0), 1)
                object_name = classLabels[class_ix - 1]
                cv2.putText(frame, object_name, (boxes[0], boxes[1]), font, fontScale=font_scale, color=(0, 255, 0), thickness=3)
                
                x_coord = int(boxes[0] + boxes[2] / 2)
                y_coord = int(boxes[1] + boxes[3] / 2)
                obj_coord = (x_coord, y_coord)
                cv2.circle(frame, obj_coord, 2, (0, 0, 225), 2)
                current_area = boxes[2] * boxes[3]

    cv2.imshow("Object Detection", frame)

    if object_name == objectName:
        if SIZE_THRESHOLD - SIZE_TOLERANCE <= current_area <= SIZE_THRESHOLD + SIZE_TOLERANCE:
            return x_coord, y_coord, current_area
        else:
            return 320 // 2, 320 // 2, current_area
    else:
        return 320 // 2, 320 // 2, current_area
