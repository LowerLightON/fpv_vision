from fpv_vision.vision.steps.base import BaseStep
from fpv_vision.vision.entities.frame import Frame
from fpv_vision.vision.tracking.tracker import Tracker
from fpv_vision.vision.tracking.tracked_object import TrackedObject
from fpv_vision.vision.entities.detected_object import DetectedObject


class ObjectTracking(BaseStep[Frame]):
    def __init__(self, max_distance: int, max_missed_frames: int, min_dt: float) -> None:
        self.tracker = Tracker(max_distance, max_missed_frames, min_dt)

    def apply(self, frame: Frame) -> Frame:
        detections: list[DetectedObject] = frame.objects
        timestamp = frame.timestamp

        objects: list[TrackedObject] = self.tracker.update(detections, timestamp)
        frame.objects = objects
        return frame
