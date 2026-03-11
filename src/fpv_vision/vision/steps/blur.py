from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar
T = TypeVar('T')

class Blur(BaseStep[T]):
    def apply(self, frame: T) -> T:
        return frame