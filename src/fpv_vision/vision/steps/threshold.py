from typing import TypeVar
from fpv_vision.vision.steps.base import BaseStep

T = TypeVar('T')
class Threshold(BaseStep[T]):
    def apply(self, frame: T) -> T:
        return frame
