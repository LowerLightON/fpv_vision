from abc import ABC, abstractmethod
from fpv_vision.vision.entities.frame import Frame

class FrameSource(ABC):
    @property
    def name(self) -> str:
        return self.__class__.__name__
    
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def read(self) -> Frame:
        pass    

    @abstractmethod
    def close(self) -> None:
        pass