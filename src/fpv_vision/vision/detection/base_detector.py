from abc import ABC, abstractmethod
from fpv_vision.vision.entities.detected_object import DetectedObject
from fpv_vision.vision.entities.frame import Frame

class Detector(ABC):
    @abstractmethod
    def detect(self, frame: Frame) -> list[DetectedObject]:
        pass