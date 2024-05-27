# config.py

# Object detection settings
OBJECT_NAME = 'mouse'
CONF_THRESHOLD = 0.55
SIZE_THRESHOLD = 10000
SIZE_TOLERANCE = 0.1 * SIZE_THRESHOLD  # 10% of the size threshold

# Camera settings
CAMERA_INDEX = 1
INPUT_SIZE = (320, 320)
INPUT_SCALE = 1 / 127.5
INPUT_MEAN = (127.5, 127.5, 127.5)
INPUT_SWAP_RB = True

# Control settings
MOVE_THRESHOLD = 5
MOVE_FORWARD_KEY = 'w'
MOVE_BACKWARD_KEY = 's'
MOVE_LEFT_KEY = 'a'
MOVE_RIGHT_KEY = 'd'
STOP_KEY = 'x'

# Paths
CONFIG_FILE = "camDetectSrcs/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
FROZEN_MODEL = "camDetectSrcs/frozen_inference_graph.pb"
LABELS_FILE = "camDetectSrcs/coco.names"
