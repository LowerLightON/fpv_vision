#Названия окон
import cv2

WIN_INT_CAMERA = 'Integrated Camera'

#Параметры камеры
CAP = {
    "device": "/dev/video0",
    "width": 1280,
    "height": 720,
    "fps": 30,
    "fourcc": "MJPG",
}