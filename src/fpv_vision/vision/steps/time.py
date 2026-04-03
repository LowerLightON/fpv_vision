import time
from fpv_vision.vision.steps.base import BaseStep, Frame

class TimeStep(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        frame.set("timestamp", time.time())
        return frame