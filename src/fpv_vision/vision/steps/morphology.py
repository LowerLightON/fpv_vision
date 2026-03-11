from fpv_vision.vision.steps.base import BaseStep
from typing import TypeVar
T = TypeVar('T')
class Morphology(BaseStep[T]):
    def apply(self, frame: T) -> T:
        return frame