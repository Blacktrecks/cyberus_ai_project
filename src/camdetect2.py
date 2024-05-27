import cv2
from pathlib import Path
from validateMBlockWin import focusToMblock
from robotControl import RobotControl
from config import *
import time

robot_control = RobotControl()

def initCamera():
    file_path = Path(__file__).parent
    config_file = file_path / CONFIG_FILE
    frozen_model = file_path / FROZEN_MODEL
    model = cv2.dnn_DetectionModel(str(frozen_model), str(config_file))
    classLabels = []
    file_name = file_path / LABELS_FILE
    with open(file_name, 'rt') as fpt:
        classLabels = fpt.read().rstrip('\n').split('\n')
    if not classLabels:
        exit(1)
    model.setInputSize(INPUT_SIZE)
    model.setInputScale(INPUT_SCALE)
    model.setInputMean(INPUT_MEAN)
    model.setInputSwapRB(INPUT_SWAP_RB)
    cap = cv2.VideoCapture(CAMERA_INDEX)
    font_scale = 1
    font = cv2.FONT_HERSHEY_PLAIN
    return cap, model, classLabels, font, font_scale

cap, model, classLabels, font, font_scale = initCamera()

def getObjectPos(objectName):
    _, frame = cap.read()
    classIndex, confidence, bbox = model.detect(frame, confThreshold=CONF_THRESHOLD)
    object_name = None
    current_area = 0

    if len(classIndex) != 0:
        for class_ix, conf, boxes in zip(classIndex.flatten(), confidence.flatten(), bbox):
            if class_ix <= 80:
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
            # Object size within the tolerance range
            return x_coord, y_coord, current_area
        else:
            # Object size outside the tolerance range, return center coordinates
            return 320 // 2, 320 // 2, current_area
    else:
        return 320 // 2, 320 // 2, current_area

def centerObject(posX, posY, current_area):
    screen_center_x = 320 // 2
    screen_center_y = 320 // 2

    error_x = screen_center_x - posX
    error_y = screen_center_y - posY

    focusToMblock()
    
    robot_control.move_robot(error_x, error_y)

    # Check size threshold with tolerance for forward/backward movement
    if current_area < SIZE_THRESHOLD - SIZE_TOLERANCE:
        robot_control.start_moving_forward()
    elif current_area > SIZE_THRESHOLD + SIZE_TOLERANCE:
        robot_control.start_moving_backward()
    else:
        robot_control.stop_moving()

    if abs(error_x) < MOVE_THRESHOLD and abs(error_y) < MOVE_THRESHOLD:
        robot_control.stop_robot()

    # Add a delay to test on-site accuracy
    time.sleep(0.2)  # 100ms delay for better accuracy testing

def robotRoutine():
    focusToMblock()
    while True:
        posX, posY, current_area = getObjectPos(OBJECT_NAME)
        print(f"x = {posX}, y = {posY}, area = {current_area}")
        centerObject(posX, posY, current_area)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()