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


