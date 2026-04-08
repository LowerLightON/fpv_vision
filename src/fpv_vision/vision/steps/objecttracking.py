from fpv_vision.vision.steps.base import BaseStep,Frame
from fpv_vision.vision.utils.geometry import distance


class ObjectTracking(BaseStep[Frame]):
    def __init__(self, max_distance: int) -> None:
        self.next_id = 1
        self.prev_objects = []
        self.max_distance = max_distance

    def apply(self, frame: Frame) -> Frame:
        current_objects = frame.objects

        if not current_objects:
            self.prev_objects = []
            return frame

        if not self.prev_objects:
            for obj in current_objects:
                obj.obj_id = self.next_id
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

                dist = distance(current_obj.center, prev_obj.center)

                if dist < self.max_distance and dist < best_dist:
                    best_dist = dist
                    best_prev_obj = prev_obj

            if best_prev_obj is not None:
                current_obj.obj_id = best_prev_obj.obj_id
                used_obj_id.add(best_prev_obj.obj_id)
            else:
                current_obj.obj_id = self.next_id
                self.next_id += 1

        self.prev_objects = current_objects.copy()
        return frame
