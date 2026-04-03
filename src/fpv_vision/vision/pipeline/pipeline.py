from typing import TypeVar, Generic
from fpv_vision.vision.steps.base import BaseStep

T = TypeVar('T')

class Pipeline(Generic[T]):
    def __init__(self, steps: list[BaseStep[T]]):
        self.steps = steps
    def __call__(self, current: T) -> T:
        return self.process(current)
    def process(self, frame: T) -> T:
        if frame is None:
            raise ValueError("Frame is None")
        current = frame
        for step in self.steps:
            current = step(current)
        return current
