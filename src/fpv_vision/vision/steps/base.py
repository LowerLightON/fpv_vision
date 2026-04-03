from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseStep(Generic[T],ABC):
    @property
    def name(self)-> str:
        return self.__class__.__name__
    def __call__(self, frame: T) -> T:
        return self.apply(frame)

    @abstractmethod
    def apply(self, frame: T) -> T:
        pass
class Frame:
    def __init__(self, image):
        self.image = image
        self.target_center = None  # (x, y) | None
        self.error = None          # (x, y) | None
        self.contour = None
        self.prev_center = None
        self.frame_center = None
        self.bounding_box = None
