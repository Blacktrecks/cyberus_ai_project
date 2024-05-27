import cv2
from pathlib import Path
from config import *

def initCamera():
    """Initialize the camera and object detection model."""
    file_path = Path(__file__).parent.parent
    config_file = file_path / CONFIG_FILE
    frozen_model = file_path / FROZEN_MODEL
    model = cv2.dnn_DetectionModel(str(frozen_model), str(config_file))

    # Load class labels
    with open(file_path / LABELS_FILE, 'rt') as fpt:
        classLabels = fpt.read().rstrip('\n').split('\n')
    if not classLabels:
        raise FileNotFoundError("Labels file not found or empty.")

    # Set model parameters
    model.setInputSize(INPUT_SIZE)
    model.setInputScale(INPUT_SCALE)
    model.setInputMean(INPUT_MEAN)
    model.setInputSwapRB(INPUT_SWAP_RB)

    # Initialize camera
    cap = cv2.VideoCapture(CAMERA_INDEX)
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1

    return cap, model, classLabels, font, font_scale
