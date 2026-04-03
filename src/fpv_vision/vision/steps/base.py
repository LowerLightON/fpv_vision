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
        self.meta = {
            "target_center" : None,
            "error" : None,
            "contour" : None,
            "prev_center" : None,
            "frame_center" : None,
            "bounding_box" : None,
        }


    def set(self, key , value):
        self.meta[key] = value

    def get(self, key , default = None):
        return self.meta.get(key, default)
