from fpv_vision.vision.steps.base import BaseStep, Frame

class ErrorStep(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        height, width = frame.image.shape[:2]
        frame.frame_center = (width // 2, height // 2)

        if frame.primary_object is None:
            frame.error = None
            return frame
        if frame.frame_center is None:
            frame.error = None
            return frame
        target_x, target_y = frame.primary_object.center
        error_x = target_x -  frame.f_x
        error_y = target_y -  frame.f_y
        frame.error = (error_x, error_y)
        return frame
