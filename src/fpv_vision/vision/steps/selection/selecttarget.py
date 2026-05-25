from fpv_vision.vision.steps.base import BaseStep
from fpv_vision.vision.entities.frame import Frame

class SelectTarget(BaseStep[Frame]):
    def apply(self, frame: Frame) -> Frame:
        if not frame.tracked_objects:
            frame.selected_target = None
            return frame
        frame.selected_target = max(frame.tracked_objects, key=lambda obj: obj.current_detection.area)
        return frame