import cv2
from fpv_vision import config as cfg
from fpv_vision.vision.source.video_file_source import VideoFileSource
from fpv_vision.vision.pipeline.build import build_pipeline

def main():
    source = VideoFileSource(cfg.VIDEO_FILE["PATH"])
    pipeline = build_pipeline()

    try:
        source.open()
        while True:
            frame = source.read()
            if frame is None:
                break
            cv2.imshow("original", frame.image)
            frame = pipeline(frame)
            cv2.imshow(cfg.WIN_INT_CAMERA, frame.image)
            cv2.imshow("mask and draw", frame.image)

            bitwise_image = frame.get_debug("bitwise_image", None)
            if bitwise_image is not None:
                cv2.imshow("bitwise image", bitwise_image)

            if cv2.waitKey(1) == 27:
                break
    finally:
        source.close()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main()