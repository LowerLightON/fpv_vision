import time
from fpv_vision.vision.steps.base import BaseStep
from fpv_vision.vision.entities.frame import Frame

class TimeStep(BaseStep[Frame]):
    def apply(self, frame: Frame) -> Frame:
        frame.timestamp = time.time()
        return frame