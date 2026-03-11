import cv2
from fpv_vision import config as cfg
from fpv_vision.vision.camera import Camera
from fpv_vision.vision.pipeline.build import build_pipeline


cam = Camera()
pipeline = build_pipeline()

try:
    cam.open()
    while True:
        frame = cam.read()
        frame = pipeline(frame)
        cv2.imshow(cfg.WIN_INT_CAMERA, frame)

        if cv2.waitKey(1) == 27:
            break
finally:
    cam.close()
    cv2.destroyAllWindows()