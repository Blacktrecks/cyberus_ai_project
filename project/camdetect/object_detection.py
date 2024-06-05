import cv2
from config import *
from .camera import initCamera
from ..config import CONF_THRESHOLD, SIZE_THRESHOLD, SIZE_TOLERANCE, MOVE_THRESHOLD, INPUT_SIZE

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

                if object_name in objectName:
                    break

    print(object_name)
    cv2.imshow("Object Detection", frame)

    screen_center_x = INPUT_SIZE[0] // 2
    screen_center_y = INPUT_SIZE[1] // 2

    if object_name in objectName:
        return x_coord, y_coord, current_area
    else:
        return screen_center_x, screen_center_y, SIZE_THRESHOLD
