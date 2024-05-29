# Object detection settings
OBJECT_NAME = 'bottle'
CONF_THRESHOLD = 0.55
SIZE_THRESHOLD = 10000
SIZE_TOLERANCE = 8000  # Tolerance for object size

# Camera settings
CAMERA_INDEX = 1
INPUT_SIZE = (640, 480)
INPUT_SCALE = 1 / 127.5
INPUT_MEAN = (127.5, 127.5, 127.5)
INPUT_SWAP_RB = True

# Control settings
MOVE_THRESHOLD = 20
MOVE_FORWARD_KEY = 'w'
MOVE_BACKWARD_KEY = 's'
MOVE_LEFT_KEY = 'a'
MOVE_RIGHT_KEY = 'd'
STOP_KEY = 'x'
MOVE_HAND_UP_KEY = 'q'
MOVE_HAND_DOWN_KEY = 'e'
STOP_HAND_KEY = 'z'

# Paths
CONFIG_FILE = "camDetectSrcs/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
FROZEN_MODEL = "camDetectSrcs/frozen_inference_graph.pb"
LABELS_FILE = "camDetectSrcs/coco.names"
