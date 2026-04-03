from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class DrawTarget(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        if frame is None:
            return ValueError("frame is None")
        x, y, w, h = frame.bounding_box
        cv2.circle(frame.image, frame.error, 5, (0, 0, 255), -1)
        cv2.circle(frame.image, frame.frame_center, 5, (255, 0, 0), -1)
        cv2.line(frame.image, frame.frame_center, frame.error, (255, 255, 0), 2)
        cv2.rectangle(frame.image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame