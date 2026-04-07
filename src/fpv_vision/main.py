import cv2
from fpv_vision import config as cfg
from fpv_vision.vision.camera import Camera
from fpv_vision.vision.pipeline.build import build_pipeline

def main():
    cam = Camera()
    pipeline = build_pipeline()

    try:
        cam.open()
        while True:
            frame = cam.read()
            frame = pipeline(frame)
            cv2.imshow(cfg.WIN_INT_CAMERA, frame.image)
            cv2.imshow("mask and draw", frame.image)
            cv2.imshow("bitwise image", frame.get_debug("bitwise_image"))

            if cv2.waitKey(1) == 27:
                break
    finally:
        cam.close()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main()