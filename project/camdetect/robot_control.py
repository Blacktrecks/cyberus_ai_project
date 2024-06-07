from pynput.keyboard import Controller
from config import *
import time

from project.config import MOVE_THRESHOLD, MOVE_RIGHT_KEY, MOVE_LEFT_KEY, MOVE_FORWARD_KEY, MOVE_BACKWARD_KEY, \
    MOVE_HAND_UP_KEY, MOVE_HAND_DOWN_KEY, STOP_KEY, STOP_HAND_KEY, SIZE_THRESHOLD, SIZE_TOLERANCE

class Direction:
    left = 0
    right = 1
    forward = 2
    backward = 3
    none = -1

class RobotControl:
    direction = Direction.none
    def __init__(self):
        self.keyboard = Controller()
        self.move_threshold = MOVE_THRESHOLD


    def start_moving_right(self):
        if(self.direction != Direction.right):
            self.stop_moving()
            self.keyboard.press(MOVE_RIGHT_KEY)
            self.direction = Direction.right
            print(f"Pressed '{MOVE_RIGHT_KEY}' for moving right")
        print(f"Skip right")

    def start_moving_left(self):
        if(self.direction != Direction.left):
            self.stop_moving()
            self.keyboard.press(MOVE_LEFT_KEY)
            self.direction = Direction.left
            print(f"Pressed '{MOVE_LEFT_KEY}' for moving left")
        print(f"Skip left")

    def start_moving_forward(self):
        if(self.direction != Direction.forward):
            self.stop_moving()
            self.keyboard.press(MOVE_FORWARD_KEY)
            self.direction = Direction.forward
            print(f"Pressed '{MOVE_FORWARD_KEY}' for moving forward")
        print(f"Skip forward")

    def start_moving_backward(self):
        if(self.direction != Direction.backward):
            self.stop_moving()
            self.keyboard.press(MOVE_BACKWARD_KEY)
            self.direction = Direction
            print(f"Pressed '{MOVE_BACKWARD_KEY}' for moving backward")
        print(f"Skip backward")

    def start_moving_hand_up(self):
        self.keyboard.press(MOVE_HAND_UP_KEY)
        print(f"Pressed '{MOVE_HAND_UP_KEY}' for moving hand up")
        pass

    def start_moving_hand_down(self):
        self.keyboard.press(MOVE_HAND_DOWN_KEY)
        print(f"Pressed '{MOVE_HAND_DOWN_KEY}' for moving hand down")
        pass

    def stop_moving(self):
        self.direction = Direction.none
        self.keyboard.release(MOVE_RIGHT_KEY)
        self.keyboard.release(MOVE_LEFT_KEY)
        self.keyboard.release(MOVE_FORWARD_KEY)
        self.keyboard.release(MOVE_BACKWARD_KEY)
        self.keyboard.press(STOP_KEY)
        self.keyboard.release(STOP_KEY)
        print("Stopped all movements")

    def stop_hand_movement(self):
        self.keyboard.release(MOVE_HAND_UP_KEY)
        self.keyboard.release(MOVE_HAND_DOWN_KEY)
        self.keyboard.press(STOP_HAND_KEY)
        self.keyboard.release(STOP_HAND_KEY)
        print("Stopped hand motor")
        pass

    def move_robot(self, error_x, error_y, current_area):
        # Horizontal movement
        print("Error x " + str(error_x) + " Error y " + str(error_y))
        if error_x > self.move_threshold:
            self.start_moving_left()
        elif error_x < -self.move_threshold:
            self.start_moving_right()

        # # Hand movement based on vertical error
        # if error_y > self.move_threshold:
        #     self.start_moving_hand_down()
        # elif error_y < -self.move_threshold:
        #     self.start_moving_hand_up()

        # Forward and backward movement based on object size
        if current_area < SIZE_THRESHOLD - SIZE_TOLERANCE:
            self.start_moving_forward()
        elif current_area > SIZE_THRESHOLD + SIZE_TOLERANCE:
            self.start_moving_backward()



    def stop_robot(self):
        self.stop_moving()
        # self.stop_hand_movement()
