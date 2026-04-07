from fpv_vision.vision.steps.base import BaseStep, Frame

class SmoothCenter(BaseStep[Frame]):
    def __init__(self, alpha: float) -> None:
        self.alpha = alpha
        self.prev_smoothed_target_center = None
    def apply(self, frame: Frame) -> Frame:
        obj = frame.primary_object

        if obj is None:
            self.prev_smoothed_target_center = None
            return frame

        if obj.center is None:
            obj.smoothed_center = None
            self.prev_smoothed_target_center = None
            return frame

        cx, cy = obj.center

        if self.prev_smoothed_target_center is None:
            smooth_center = (cx, cy)
        else:
            prev_x, prev_y = self.prev_smoothed_target_center

            smooth_x = int(prev_x * self.alpha + cx * (1 - self.alpha))
            smooth_y = int(prev_y * self.alpha + cy * (1 - self.alpha))
            smooth_center = (smooth_x, smooth_y)

        obj.smoothed_center = smooth_center
        self.prev_smoothed_target_center = smooth_center
        return frame

