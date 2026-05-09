from fpv_vision.vision.steps.base import BaseStep
from fpv_vision.vision.entities.frame import Frame

class SelectPrimaryObject(BaseStep[Frame]):
    def apply(self, frame: Frame) -> Frame:
        if not frame.objects:
            frame.primary_object = None
            return frame
        frame.primary_object = max(frame.objects, key = lambda obj: obj.current_detection.area or 0)
        return frame