from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class TargetAndSmoothCenter(BaseStep[Frame]):
    def __init__(self) -> None:
        self.prev_smoothed_target_center = None
    def apply(self, frame: Frame) -> Frame:
        contour = frame.get("contour")
        if contour is None:
            frame.set("raw_target_center",  None)
            frame.set("bounding_box", None)
            frame.set("smoothed_target_center", None)
            return frame

        frame.set("bounding_box" , cv2.boundingRect(frame.get("contour")))
        x, y, w, h = frame.get("bounding_box")
        m = cv2.moments(frame.get("contour"))
        if m["m00"] != 0:
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
        else:
            cx = x + w // 2
            cy = y + h // 2

        frame.set("raw_target_center", (cx, cy))

        if self.prev_smoothed_target_center is None:
            smooth_center = (cx, cy)
        else:
            smooth_x = int(self.prev_smoothed_target_center[0] * 0.8 + cx * 0.2)
            smooth_y = int(self.prev_smoothed_target_center[1] * 0.8 + cy * 0.2)
            smooth_center = (smooth_x, smooth_y)

        frame.set("smoothed_target_center", smooth_center)

        self.prev_smoothed_target_center = smooth_center
        return frame

