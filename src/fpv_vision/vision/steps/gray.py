from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar
T = TypeVar('T')
import cv2
class Grayscale(BaseStep[T]):
    def __init__(self, color_code: int ) -> None:
        self.color_code = color_code
    def apply(self, frame: T) -> T:
        if frame is None:
            raise ValueError('frame is None')
        frame = cv2.cvtColor(frame, self.color_code)
        return frame