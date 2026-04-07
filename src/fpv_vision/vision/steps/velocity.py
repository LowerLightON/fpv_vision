from fpv_vision.vision.steps.base import BaseStep,Frame
import math

class VelocityStep(BaseStep[Frame]):
    def __init__(self, alpha: float) -> None:
        self.prev_timestamp = None
        self.prev_center = None
        self.prev_velocity = None
        self.alpha = alpha

    def apply(self, frame: Frame) -> Frame:
        if frame.primary_object is None:
            self.prev_timestamp = None
            self.prev_center = None
            self.prev_velocity = None
            return frame
        current_center = frame.primary_object.center
        current_timestamp = frame.timestamp

        if current_center is None or current_timestamp is None:
            frame.primary_object.velocity = None
            self.prev_center = None
            self.prev_timestamp = None
            self.prev_velocity = None
            return frame
        if self.prev_timestamp is None or self.prev_center is None:
            frame.primary_object.velocity = None
            self.prev_timestamp = current_timestamp
            self.prev_center = current_center
            return frame

        dt = current_timestamp - self.prev_timestamp

        if dt <= 0:
            frame.primary_object.velocity = None
            self.prev_timestamp = current_timestamp
            self.prev_center = current_center
            return frame
        dx = current_center[0] - self.prev_center[0]
        dy = current_center[1] - self.prev_center[1]

        vx = dx / dt
        vy = dy / dt

        if self.prev_velocity is None:
           smooth_velocity = (vx, vy)
        else:
            vx_s = self.prev_velocity[0] * self.alpha + vx * (1 - self.alpha)
            vy_s = self.prev_velocity[1] * self.alpha + vy * (1 - self.alpha)
            smooth_velocity = (vx_s, vy_s)
        frame.primary_object.velocity = smooth_velocity

        vx_s, vy_s = smooth_velocity
        if frame.primary_object.velocity  is None:
            frame.primary_object.angle = None
        else:
            angle = math.atan2(vy_s, vx_s)
            frame.primary_object.angle = angle

        self.prev_timestamp = current_timestamp
        self.prev_center = current_center
        self.prev_velocity = smooth_velocity
        return frame

