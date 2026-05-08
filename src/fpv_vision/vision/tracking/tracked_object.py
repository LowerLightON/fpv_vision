class TrackedObject:
    def __init__(self, obj_id: int, detection: object, timestamp: float):
        self._obj_id = obj_id
        self.current_detection = detection
        self.previous_center = None
        self.current_center = detection.center

        self.velocity = None
        self.predicted_center = None
        self._missed_frames = 0
        self.last_timestamp = timestamp

    @property
    def obj_id(self) -> int:
        return self._obj_id

    @property
    def missed_frames(self) -> int:
        return self._missed_frames

    def update(self, detection, timestamp):
        self.previous_center = self.current_center
        self.current_center = detection.center
        self.current_detection = detection
        self._missed_frames = 0

        previous_timestamp = self.last_timestamp
        dt = timestamp - previous_timestamp
        self.last_timestamp = timestamp
        if dt <= 0:


    def mark_missed(self):
        self._missed_frames += 1

    def is_lost(self,  max_missed_frames) -> bool:
        return self.missed_frames > max_missed_frames
