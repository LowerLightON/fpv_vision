from fpv_vision.vision.steps.base import BaseStep,Frame
from fpv_vision.vision.tracking.tracker import Tracker


class ObjectTracking(BaseStep[Frame]):
    def __init__(self, max_distance: int, max_missed_frames: int, min_dt: float) -> None:
        self.tracker = Tracker(max_distance, max_missed_frames, min_dt)

    def apply(self, frame: Frame) -> Frame:
        detections = frame.objects
        timestamp = frame.timestamp

        objects = self.tracker.update(detections, timestamp)
        frame.objects = objects
        return frame
