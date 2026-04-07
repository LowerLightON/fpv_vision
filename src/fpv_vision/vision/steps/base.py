from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any
from fpv_vision.vision.steps.detectedobject import DetectedObject


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

        self.timestamp: float | None = None
        self.debug_data: dict[str, Any]  = {}

        self.objects: list[DetectedObject] = []
        self.primary_object: DetectedObject | None = None

        self.frame_center: tuple[int, int] | None = None
        self.error: tuple[int, int] | None = None

    def set_debug(self, key: str , value: object) -> None:
        self.debug_data[key] = value

    def get_debug(self, key: str , default = None):
        return self.debug_data.get(key, default)

    @property
    def f_x(self) -> int:
        return self.frame_center[0] if self.frame_center else None

    @property
    def f_y(self) -> int:
        return self.frame_center[1] if self.frame_center else None
