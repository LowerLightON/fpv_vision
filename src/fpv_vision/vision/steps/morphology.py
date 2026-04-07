import cv2
import numpy as np
from fpv_vision.vision.steps.base import BaseStep, Frame
from typing import TypeVar

T = TypeVar('T')

class Morphology(BaseStep[Frame]):
    def __init__(self, kernel_size: int, operation: int):
        self.kernel_size = kernel_size
        self.operation = operation
    def apply(self, frame: Frame) -> Frame:
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        frame.image= cv2.morphologyEx(frame.image, self.operation, kernel)
        return frame
