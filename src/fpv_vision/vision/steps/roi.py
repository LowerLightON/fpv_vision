from fpv_vision.vision.steps.base import BaseStep, Frame

class ROIStep(BaseStep):
    def apply(self, frame:Frame) -> Frame:
        if frame.image is None:
            raise ValueError("Frame is None")

        height, width = frame.image.shape[:2]
        x1 = width // 4
        x2 = width * 3 // 4

        y1 = height // 4
        y2 = height * 3 // 4

        frame.image = frame.image[y1:y2, x1:x2]
        return frame