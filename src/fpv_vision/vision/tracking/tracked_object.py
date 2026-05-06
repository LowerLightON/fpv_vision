class TrackedObject:
    def __init__(self, obj_id: int, detection: object, timestamp: float):
        self.obj_id = obj_id
        self.current_detection = detection
        self.previous_center = None
        self.current_center = detection.center

        self.velocity = None
        self.predicted_center = None
        self.missed_frames = 0
        self.last_timestamp = timestamp

    @property
    def obj_id(self) -> int:
        return self.obj_id

    def update(self, detection, timestamp):
        pass

    def mark_missed(self):
        pass

    def is_lost(self,  max_missed_frames) -> bool:
        pass
