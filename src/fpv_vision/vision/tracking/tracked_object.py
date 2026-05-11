from vision.entities.detected_object import DetectedObject
class TrackedObject:
    def __init__(self, obj_id: int, detection: DetectedObject, timestamp: float, min_dt: float):
        self._obj_id = obj_id
        self.current_detection = detection
        self.previous_center = None
        self.current_center = detection.center
        self.min_dt = min_dt

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
            return
        if dt < self.min_dt:
            return

        if self.previous_center is not None:
            dx = self.current_center[0] - self.previous_center[0]
            dy = self.current_center[1] - self.previous_center[1]
            vx = dx / dt
            vy = dy / dt

            self.velocity = (vx, vy)
    def predict(self, dt: float):
        if dt is None or self.velocity is None:
            self.predicted_center = self.current_center
            return self.predicted_center

        predict_x = self.current_center[0] + self.velocity[0] * dt
        predict_y = self.current_center[1] + self.velocity[1] * dt
        self.predicted_center = (predict_x, predict_y)
        return self.predicted_center


    def mark_missed(self):
        self._missed_frames += 1

    def should_remove(self,  max_missed_frames) -> bool:
        return self.missed_frames > max_missed_frames
