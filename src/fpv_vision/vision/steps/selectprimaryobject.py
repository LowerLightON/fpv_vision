from fpv_vision.vision.steps.base import BaseStep, Frame

class SelectPrimaryObject(BaseStep[Frame]):
    def apply(self, frame: Frame) -> Frame:
        if not frame.objects:
            frame.primary_object = None
            return frame
        frame.primary_object = max(frame.objects, key = lambda obj: obj.area)
        return frame