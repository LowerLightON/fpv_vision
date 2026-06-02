from __future__ import annotations
from typing import Any

class DetectedObject:
    def __init__(self,
                 bounding_box: tuple[ int, int, int, int],
                 center: tuple[int,int],
                 area: float,
                 contour: Any | None = None
                 ) -> None:
        self.contour = contour 
        self.bounding_box = bounding_box
        self.center = center
        self.area = area

    @property
    def x(self) -> int:
        return self.center[0]

    @property
    def y(self) -> int:
        return self.center[1]

    @property
    def w(self) -> int:
        return self.bounding_box[2]

    @property
    def h(self) -> int:
        return self.bounding_box[3]