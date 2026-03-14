from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar
import cv2
T = TypeVar('T')
class Resize(BaseStep[T]):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    def apply(self, frame: T) -> T:
        if frame is None:
            raise ValueError('frame is None')
        frame = cv2.resize(frame, (self.width, self.height))
        return frame