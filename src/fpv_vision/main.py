import cv2
import config as cfg
import vision.camera as camera

cam = camera.Camera()

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