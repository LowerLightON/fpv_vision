import cv2
from fpv_vision.vision.steps.base import BaseStep, Frame

class ContoursStep(BaseStep):
    def __init__(self, min_area : float, retrieval_mode: int, approximation_method: int) -> None:
        self.min_area = min_area
        self.retrieval_mode = retrieval_mode
        self.approximation_method = approximation_method
    def apply(self, frame : Frame) ->Frame:
        if frame is None:
            raise ValueError('frame is None')
        if len(frame.image.shape) != 2:
            raise ValueError("ContoursStep expects grayscale/binary image")
        contours, _ = cv2.findContours(frame.image, self.retrieval_mode,self.approximation_method)
        if not contours:
            frame.set("prev_center", None )
            frame.set("error",   None)
            frame.set("target_center",  None)
            frame.set("contour",  None)
            frame.set("bounding_box",  None)
            frame.image = cv2.cvtColor(frame.image, cv2.COLOR_GRAY2BGR)
            return frame

        biggest_contour = None
        biggest_area = 0.0

        for contour in contours:
            area = cv2.contourArea(contour)

            if area < self.min_area:
                continue

            if area > biggest_area:
                biggest_area = area
                biggest_contour = contour

        frame.image = cv2.cvtColor(frame.image, cv2.COLOR_GRAY2BGR)

        if biggest_contour is None:
            frame.set("prev_center", None)
            frame.set("error", None)
            frame.set("target_center", None)
            frame.set("contour", None)
            frame.set("bounding_box", None)
            return frame

        frame.set("contour", biggest_contour)
        return frame
