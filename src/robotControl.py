from pynput.keyboard import Controller
from config import *
import time

class RobotControl:
    def __init__(self):
        self.keyboard = Controller()
        self.move_threshold = MOVE_THRESHOLD

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

    def start_moving_hand_up(self):
        self.keyboard.press(MOVE_HAND_UP_KEY)
        print(f"Pressed '{MOVE_HAND_UP_KEY}' for moving hand up")

    def start_moving_hand_down(self):
        self.keyboard.press(MOVE_HAND_DOWN_KEY)
        print(f"Pressed '{MOVE_HAND_DOWN_KEY}' for moving hand down")

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

    def stop_hand_movement(self):
        self.keyboard.release(MOVE_HAND_UP_KEY)
        print(f"Released '{MOVE_HAND_UP_KEY}'")
        self.keyboard.release(MOVE_HAND_DOWN_KEY)
        print(f"Released '{MOVE_HAND_DOWN_KEY}'")
        self.keyboard.press(STOP_HAND_KEY)
        self.keyboard.release(STOP_HAND_KEY)
        print(f"Pressed and released '{STOP_HAND_KEY}' for stopping hand motor")

    def move_robot(self, error_x, error_y):
        self.stop_moving()
        if error_x > self.move_threshold:
            self.start_moving_right()
        elif error_x < -self.move_threshold:
            self.start_moving_left()

        # Hand movement based on vertical error
        if error_y > self.move_threshold:
            self.start_moving_hand_up()
        elif error_y < -self.move_threshold:
            self.start_moving_hand_down()

    def adjust_hand(self, error_y):
        self.stop_hand_movement()
        if error_y > self.move_threshold:
            self.start_moving_hand_up()
        elif error_y < -self.move_threshold:
            self.start_moving_hand_down()

    def stop_robot(self):
        self.stop_moving()
        self.stop_hand_movement()
