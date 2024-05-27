import cv2
import time
from camdetect.object_detection import getObjectPos
from camdetect.robot_control import RobotControl
from config import *
from utils.window_focus import focusToMblock

robot_control = RobotControl()

def centerObject(posX, posY, current_area):
    """
    Adjust the robot's position to center the detected object.
    
    :param posX: x-coordinate of the object's center.
    :param posY: y-coordinate of the object's center.
    :param current_area: Area of the detected object's bounding box.
    """
    screen_center_x = INPUT_SIZE[0] // 2
    screen_center_y = INPUT_SIZE[1] // 2

    error_x = screen_center_x - posX
    error_y = screen_center_y - posY

    focusToMblock()

    robot_control.move_robot(error_x, error_y, current_area)

    if abs(error_x) < MOVE_THRESHOLD and abs(error_y) < MOVE_THRESHOLD:
        robot_control.stop_robot()

    #time.sleep(0.2)  # 200ms delay for better accuracy testing

def robotRoutine():
    """
    Main routine to continuously detect and center the object.
    """
    focusToMblock()
    while True:
        posX, posY, current_area = getObjectPos(OBJECT_NAME)
        print(f"x = {posX}, y = {posY}, area = {current_area}")
        centerObject(posX, posY, current_area)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
