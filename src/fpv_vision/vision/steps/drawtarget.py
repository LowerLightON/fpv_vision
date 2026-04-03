from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class DrawTarget(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        if frame is None:
            raise ValueError("frame is None")

        if frame.get("target_center") is not None:
            cv2.circle(frame.image, frame.get("target_center"), 5, (0, 0, 255), -1)

        if frame.get("frame_center") is not None:
            cv2.circle(frame.image, frame.get("frame_center"), 5, (255, 0, 0), -1)

        if frame.get("frame_center") is not None and frame.get("target_center") is not None:
            cv2.line(frame.image, frame.get("frame_center"), frame.get("target_center"), (255, 255, 0), 2)

        if frame.get("bounding_box") is not None:
            x, y, w, h = frame.get("bounding_box")
            cv2.rectangle(frame.image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame