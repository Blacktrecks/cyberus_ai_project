from pynput.keyboard import Controller
from config import *

class RobotControl:
    def __init__(self):
        self.keyboard = Controller()
        self.move_threshold = MOVE_THRESHOLD
        self.prev_area = 0  # Initialize prev_area attribute

    def start_moving_right(self):
        self.keyboard.press(MOVE_RIGHT_KEY)
        print(f"Pressed '{MOVE_RIGHT_KEY}' for moving right")

    def start_moving_left(self):
        self.keyboard.press(MOVE_LEFT_KEY)
        print(f"Pressed '{MOVE_LEFT_KEY}' for moving left")

    def start_moving_forward(self):
        self.keyboard.press(MOVE_FORWARD_KEY)
        print(f"Pressed '{MOVE_FORWARD_KEY}' for moving forward")

    def start_moving_backward(self):
        self.keyboard.press(MOVE_BACKWARD_KEY)
        print(f"Pressed '{MOVE_BACKWARD_KEY}' for moving backward")

    def stop_moving(self):
        self.keyboard.release(MOVE_RIGHT_KEY)
        print(f"Released '{MOVE_RIGHT_KEY}'")
        self.keyboard.release(MOVE_LEFT_KEY)
        print(f"Released '{MOVE_LEFT_KEY}'")
        self.keyboard.release(MOVE_FORWARD_KEY)
        print(f"Released '{MOVE_FORWARD_KEY}'")
        self.keyboard.release(MOVE_BACKWARD_KEY)
        print(f"Released '{MOVE_BACKWARD_KEY}'")
        self.keyboard.press(STOP_KEY)
        self.keyboard.release(STOP_KEY)
        print(f"Pressed and released '{STOP_KEY}' for stopping all movements")

    def move_robot(self, error_x, error_y, current_area, prev_area):
        self.stop_moving()
        if error_x > self.move_threshold:
            self.start_moving_right()
        elif error_x < -self.move_threshold:
            self.start_moving_left()

        if current_area < SIZE_THRESHOLD:
            self.start_moving_forward()
        elif current_area > SIZE_THRESHOLD:
            self.start_moving_backward()

    def stop_robot(self):
        self.stop_moving()
