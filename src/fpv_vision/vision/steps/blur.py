from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar
import cv2
T = TypeVar('T')

class Blur(BaseStep[T]):
    def __init__(self, kernel_size: tuple[int, int] , sigma: float) -> None:
        self.kernel_size = kernel_size
        self.sigma = sigma
    def apply(self, frame: T) -> T:
        if frame is None:
            raise ValueError('frame is None')
        frame = cv2.GaussianBlur(frame, self.kernel_size, self.sigma)
        return frame