import cv2
import numpy as np
from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar

T = TypeVar('T')

class Morphology(BaseStep[T]):
    def __init__(self, kernel_size: int, operation: int):
        self.kernel_size = kernel_size
        self.operation = operation
    def apply(self, frame: T) -> T:
        if frame is None:
            raise ValueError('frame is None')
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        frame = cv2.morphologyEx(frame, self.operation, kernel)
        return frame