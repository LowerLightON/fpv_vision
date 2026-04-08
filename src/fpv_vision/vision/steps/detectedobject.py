from __future__ import annotations
from typing import Any

class DetectedObject:
    def __init__(self,
                 contour: Any,
                 bounding_box: tuple[ int, int, int, int],
                 center: tuple[int,int],
                 area: float,
                 ) -> None:
        self.contour = contour
        self.bounding_box = bounding_box
        self.center = center
        self.area = area

        self.smoothed_center: tuple[int, int] | None = None
        self.velocity: tuple[float, float] | None = None
        self.angle: float | None = None
        self.predicted_center: tuple[int, int] | None = None

        self.obj_id: int | None = None

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

    @property
    def v_x(self) -> float:
        return self.velocity[0] if self.velocity else None

    @property
    def v_y(self) -> float:
        return self.velocity[1] if self.velocity else None

    @property
    def s_x(self) -> int:
        return self.smoothed_center[0] if self.smoothed_center else None

    @property
    def s_y(self) -> int:
        return self.smoothed_center[1] if self.smoothed_center else None