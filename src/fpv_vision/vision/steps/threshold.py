from typing import TypeVar
from fpv_vision.vision.steps.base import BaseStep

import cv2

T = TypeVar('T')
class Threshold(BaseStep[T]):
    def __init__(self, threshold_value: int, max_value: int, threshold_type: int) -> None:
        self.threshold_value = threshold_value
        self.max_value = max_value
        self.threshold_type = threshold_type
    def apply(self, frame: T) -> T:
        if frame is None:
            raise ValueError('frame is None')
        _, frame = cv2.threshold(frame, self.threshold_value, self.max_value, self.threshold_type )
        return frame
