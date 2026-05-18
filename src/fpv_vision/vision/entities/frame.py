from fpv_vision.vision.entities.detected_object import DetectedObject
from typing import Any

class Frame:
    def __init__(self, image):
        self.image = image

        self.timestamp: float | None = None
        self.debug_data: dict[str, Any]  = {}

        self.detections: list[DetectedObject] = []
        self.selected_target: DetectedObject | None = None

        self.frame_center: tuple[int, int] | None = None
        self.target_offset: tuple[int, int] | None = None

    def set_debug(self, key: str , value: object) -> None:
        self.debug_data[key] = value

    def get_debug(self, key: str , default = None):
        return self.debug_data.get(key, default)

    @property
    def frame_center_x(self) -> int:
        return self.frame_center[0] if self.frame_center else None

    @property
    def frame_center_y(self) -> int:
        return self.frame_center[1] if self.frame_center else None
