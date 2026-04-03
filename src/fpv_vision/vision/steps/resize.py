from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar
import cv2

from vision.steps.base import Frame

T = TypeVar('T')
class Resize(BaseStep[T]):
    def __init__(self, width: int , height: int) -> None:
        self.width = width
        self.height = height
    def apply(self, frame: Frame) -> Frame:
        if frame.image is None:
            raise ValueError('frame is None')
        frame.image = cv2.resize(frame.image, (self.width, self.height))
        return frame