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
            "angle" : None,
            "raw_target_center" : None,
            "smoothed_target_center": None,
            "error" : None,
            "contour" : None,
            "frame_center" : None,
            "bounding_box" : None,
            "timestamp" : None,
            "velocity" : None,
        }


    def set(self, key , value):
        self.meta[key] = value

    def get(self, key , default = None):
        return self.meta.get(key, default)
