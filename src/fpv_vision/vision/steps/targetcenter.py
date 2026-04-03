from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class TargetAndSmoothCenter(BaseStep[Frame]):
    def apply(self, frame: Frame) -> Frame:
        if frame is None:
            raise ValueError("Frame is None")

        frame.bounding_box = cv2.boundingRect(frame.contour)
        x, y, w, h = frame.bounding_box
        m = cv2.moments(frame.contour)
        if m["m00"] != 0:
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
        else:
            cx = x + w // 2
            cy = y + h // 2

        frame.target_center = (cx, cy)

        if frame.prev_center is None:
            smooth_center = (cx, cy)
        else:
            smooth_x = int(frame.prev_center[0] * 0.8 + cx * 0.2)
            smooth_y = int(frame.prev_center[1] * 0.8 + cy * 0.2)
            smooth_center = (smooth_x, smooth_y)

        frame.prev_center = smooth_center
        frame.target_center = smooth_center
        return frame

