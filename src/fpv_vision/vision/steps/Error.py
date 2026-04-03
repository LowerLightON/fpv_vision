from fpv_vision.vision.steps.base import BaseStep, Frame

class ErrorStep(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        if frame is None:
            raise ValueError("Frame is None")
        height, width = frame.image.shape[:2]
        frame.frame_center = (width // 2, height // 2)


        if frame.target_center is None:
            frame.error = None
            return frame

        target_x, target_y = frame.target_center
        error_x = target_x - frame.frame_center[0]
        error_y = target_y - frame.frame_center[1]
        frame.error = (error_x, error_y)
        return frame
