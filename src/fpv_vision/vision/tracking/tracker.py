from fpv_vision.vision.utils.geometry import distance as calculate_distance
from fpv_vision.vision.tracking.tracked_object import TrackedObject
class Tracker:
	def __init__(self, max_distance: int, max_missed_frames: int):
		self.objects = []
		self.next_id = 1

		self.max_distance = max_distance
		self.max_missed_frames = max_missed_frames

	def update(self, detections, timestamp):
		used_objects = set()
		for detection in detections:
			best_object = None
			best_distance = self.max_distance

			for obj in self.objects:
				if obj.obj_id in used_objects:
					continue

				distance = calculate_distance(detection.center, obj.current_center)

				if distance < best_distance:
					best_object = obj
					best_distance = distance

			if best_object is not None:
				best_object.update(detection, timestamp)
				used_objects.add(best_object.obj_id)
			else:
				obj = TrackedObject(self.next_id, detection , timestamp)
				self.objects.append(obj)
				used_objects.add(obj.obj_id)
				self.next_id += 1

		for obj in self.objects:
			if obj.obj_id not in used_objects:
				obj.mark_missed()

		active_objects = []
		for obj in self.objects:
			if not obj.is_lost(self.max_missed_frames):
				active_objects.append(obj)
		self.objects = active_objects



