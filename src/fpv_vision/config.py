import cv2

#Названия окон
WIN_INT_CAMERA = 'Integrated Camera'

#Параметры камеры
CAP = {
    "DEVICE": "/dev/video0",
    "WIDTH": 1280,
    "HEIGHT": 720,
    "FPS": 30,
}
#Размытие blur
blur = {
    "KERNEL_SIZE": (5, 5),
    "SIGMA": 5
}

#Пороговая обработка
threshold = {
    "THRESHOLD" : 120,
    "MAX_VALUE" : 255,
    "TYPE" : cv2.THRESH_BINARY
}

#Конвертация в другие цвета
CVTCOLOR = {
    "COLOR": cv2.COLOR_BGR2GRAY,
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