from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class Resize(BaseStep[Frame]):
    def __init__(self, width: int , height: int) -> None:
        self.width = width
        self.height = height
    def apply(self, frame: Frame) -> Frame:
        frame.image = cv2.resize(frame.image, (self.width, self.height))
        return frame