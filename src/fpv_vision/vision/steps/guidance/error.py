from fpv_vision.vision.steps.base import BaseStep
from fpv_vision.vision.entities.frame import Frame

class ErrorStep(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        height, width = frame.image.shape[:2]
        frame.frame_center = (width // 2, height // 2)

        if frame.selected_target is None:
            frame.target_offset = None
            return frame
        if frame.frame_center is None:
            frame.target_offset = None
            return frame
        target_x, target_y = frame.selected_target.center
        offset_x = target_x -  frame.frame_center[0]
        offset_y = target_y -  frame.frame_center[1]
        frame.target_offset = (offset_x, offset_y)
        return frame
