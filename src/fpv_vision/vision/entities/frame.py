from fpv_vision.vision.entities.detected_object import DetectedObject
from fpv_vision.vision.tracking.tracked_object import TrackedObject
from typing import Any

class Frame:
    def __init__(self, image, timestamp: float) -> None:
        self.image = image
        self.timestamp: float = timestamp
        self.debug_data: dict[str, Any]  = {}

        self.detections: list[DetectedObject] = []
        self.tracked_objects: list[TrackedObject] = []
        self.selected_target: TrackedObject | None = None

        self.frame_center: tuple[int, int] | None = None
        self.target_offset: tuple[int, int] | None = None

    def set_debug(self, key: str , value: object) -> None:
        self.debug_data[key] = value

    def get_debug(self, key: str , default):
        return self.debug_data.get(key, default)

    @property
    def frame_center_x(self) -> int | None:
        return self.frame_center[0] if self.frame_center else None

    @property
    def frame_center_y(self) -> int | None:
        return self.frame_center[1] if self.frame_center else None
