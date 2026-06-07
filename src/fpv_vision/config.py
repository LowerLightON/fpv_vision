import cv2

#Названия окон
WIN_INT_CAMERA = 'Integrated Camera'

#Параметры камеры
CAM = {
    "DEVICE": "/dev/video0",
    "WIDTH": 1280,
    "HEIGHT": 720,
    "FPS": 30,
}

#Параметры видеофайла
VIDEO_FILE = {
    "PATH": "data/videos/test_1.mp4",
}

#Morphology
MORPH_PARAMS = {
    "KERNEL_SIZE": 3,
    "OPERATION": cv2.MORPH_OPEN
}

#FindContours
FIND_CONTOUR_PARAMS = {
    "MIN_AREA": 100,
    "RETRIEVAL": cv2.RETR_EXTERNAL,
    "APPROXIMATION": cv2.CHAIN_APPROX_SIMPLE
}

#HSV Mask
HSV_MASK = {
    "LOWER": (30, 40, 30),
    "UPPER": (95, 255, 255)
}

#TrackingObject
MAX_DISTANCE = 30
MAX_MISSED_FRAMES = 5
MIN_DT = 1

#MetricCollector
HISTORY_SIZE = 120

#Tracker
IOU_WEIGHT = 100

#Yolo
YOLO = {
    "MODEL_PATH": "yolo11n.onnx",
    "CONFIDENCE": 0.25,
    "INPUT_SIZE": 640,
    "ALLOWED_CLASS_IDS": {2, 3, 5, 7}
}