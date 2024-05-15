import cv2
from pathlib import Path

# Get Absolute Path of the executed file
file_path = Path(__file__).parent

# Create an absolute file path to the sources required
config_file = file_path.__str__() + "/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = file_path.__str__() + "/frozen_inference_graph.pb"

model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
file_name = file_path.__str__() + "/coco.names"
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

if not classLabels:
    exit(1)

model.setInputSize(320, 320)
model.setInputScale(1 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

cap = cv2.VideoCapture(0)

font_scale = 1
font = cv2.FONT_HERSHEY_PLAIN

while True:
    ret, frame = cap.read()

    classIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)

    # print(classIndex)

    if len(classIndex) != 0:
        for class_ix, conf, boxes in zip(classIndex.flatten(), confidence.flatten(), bbox):
            if class_ix <= 80:
                cv2.rectangle(
                    frame,
                    boxes,
                    (225, 0, 0),
                    1
                )

                object_name = classLabels[class_ix - 1]

                cv2.putText(
                    frame,
                    object_name,
                    (boxes[0], boxes[1]),
                    font,
                    fontScale=font_scale,
                    color=(0, 255, 0),
                    thickness=3
                )

                x_coord = int(boxes[0] + boxes[2] / 2)
                y_coord = int(boxes[1] + boxes[3] / 2)
                obj_coord = (x_coord, y_coord)

                cv2.circle(
                    frame,
                    obj_coord,
                    2,
                    (0, 0, 225),
                    2
                )

                if object_name == 'cell phone':
                    print(object_name, 'at', obj_coord)

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
