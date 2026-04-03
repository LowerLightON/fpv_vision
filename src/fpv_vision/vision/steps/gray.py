from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar

from vision.steps.base import Frame

T = TypeVar('T')
import cv2
class Grayscale(BaseStep[T]):
    def __init__(self, color_code: int ) -> None:
        self.color_code = color_code
    def apply(self, frame: Frame) -> Frame:
        if frame.image is None:
            raise ValueError('frame is None')
        frame.image = cv2.cvtColor(frame.image, self.color_code)
        return frame