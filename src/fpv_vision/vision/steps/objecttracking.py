from fpv_vision.vision.steps.base import BaseStep,Frame
from fpv_vision.vision.utils.geometry import distance


class ObjectTracking(BaseStep[Frame]):
    def __init__(self, max_distance: int, max_missed_frames: int) -> None:
        self.next_id = 1
        self.prev_objects = []
        self.max_distance = max_distance

        self.missed_frames = {}
        self.max_missed_frames = max_missed_frames

    def apply(self, frame: Frame) -> Frame:
        current_objects = frame.objects

        if not self.prev_objects:
            for obj in current_objects:
                obj.obj_id = self.next_id
                self.missed_frames[obj.obj_id] = 0
                self.next_id += 1

            self.prev_objects = current_objects.copy()
            return frame

        used_obj_id = set()
        for current_obj in current_objects:
            best_prev_obj = None
            best_dist = float('inf')

            for prev_obj in self.prev_objects:
                if prev_obj.obj_id in used_obj_id:
                    continue

                prev_point = prev_obj.predicted_center

                if prev_point is None:
                    prev_point = prev_obj.center

                dist = distance(current_obj.center, prev_point)

                if dist < self.max_distance and dist < best_dist:
                    best_dist = dist
                    best_prev_obj = prev_obj

            if best_prev_obj is not None:
                current_obj.obj_id = best_prev_obj.obj_id
                used_obj_id.add(best_prev_obj.obj_id)

                self.missed_frames[current_obj.obj_id] = 0
            else:
                current_obj.obj_id = self.next_id
                self.next_id += 1

                self.missed_frames[current_obj.obj_id] = 0

        for prev_obj in self.prev_objects:
            obj_id = prev_obj.obj_id
            if obj_id not in used_obj_id:
                self.missed_frames.setdefault(obj_id, 0)
                self.missed_frames[obj_id] += 1

        new_prev_obj = []
        for obj in current_objects:
            new_prev_obj.append(obj)

        for prev_obj in self.prev_objects:
            obj_id = prev_obj.obj_id

            if obj_id in used_obj_id:
                continue

            if self.missed_frames.get(obj_id, 0) <= self.max_missed_frames:
                new_prev_obj.append(prev_obj)

        self.prev_objects = new_prev_obj
        return frame
