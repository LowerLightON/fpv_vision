from fpv_vision.vision.steps.base import BaseStep,Frame

class PredictionStep(BaseStep[Frame]):
    def __init__(self, predicted_time: float) -> None:
        self.predicted_time = predicted_time
    def apply(self, frame: Frame) -> Frame:
        if frame.primary_object is None:
            return frame
        center = frame.primary_object.smoothed_center
        velocity = frame.primary_object.velocity

        if center is None or velocity is None:
            frame.primary_object.predicted_center = None
            return frame

        x, y = center
        vx, vy = velocity

        p_x = int(x + vx * self.predicted_time)
        p_y = int(y + vy * self.predicted_time)
        frame.primary_object.predicted_center = (p_x, p_y)
        return frame