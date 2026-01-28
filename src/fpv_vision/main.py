import cv2
from fpv_vision import config as cfg
from fpv_vision.vision.camera import Camera

cam = Camera()

try:
    cam.open()
    while True:
        frame = cam.read()
        cv2.imshow(cfg.WIN_INT_CAMERA, frame)

        if cv2.waitKey(1) == 27:
            break
finally:
    cam.close()
    cv2.destroyAllWindows()