from fpv_vision.vision.steps.base import BaseStep, Frame
from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class DrawTarget(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        if frame is None:
            raise ValueError("frame is None")

        if frame.target_center is not None:
            cv2.circle(frame.image, frame.target_center, 5, (0, 0, 255), -1)

        if frame.frame_center is not None:
            cv2.circle(frame.image, frame.frame_center, 5, (255, 0, 0), -1)

        if frame.frame_center is not None and frame.target_center is not None:
            cv2.line(frame.image, frame.frame_center, frame.target_center, (255, 255, 0), 2)

        if frame.bounding_box is not None:
            x, y, w, h = frame.bounding_box
            cv2.rectangle(frame.image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame