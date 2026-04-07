import cv2
from fpv_vision.vision.steps.base import BaseStep, Frame

class ContoursStep(BaseStep[Frame]):
    def __init__(self, min_area : float, retrieval_mode: int, approximation_method: int) -> None:
        self.min_area = min_area
        self.retrieval_mode = retrieval_mode
        self.approximation_method = approximation_method
    def apply(self, frame : Frame) ->Frame:
        if len(frame.image.shape) != 2:
            raise ValueError("ContoursStep expects grayscale/binary image")
        contours, _ = cv2.findContours(frame.image, self.retrieval_mode,self.approximation_method)

        valid_contours = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area >= self.min_area:
                valid_contours.append(contour)

        frame.set_debug("contours", valid_contours)
        frame.image = cv2.cvtColor(frame.image, cv2.COLOR_GRAY2BGR)
        return frame
