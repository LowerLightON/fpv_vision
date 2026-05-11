from fpv_vision.vision.entities.detected_object import DetectedObject
from fpv_vision.vision.tracking.tracked_object import TrackedObject
from fpv_vision.vision.utils.geometry import distance as calc_distance

class Tracker:
	def __init__(self, max_distance: float, max_missed_frames: float, min_dt: float) -> None:
		self.tracks: list[TrackedObject] = []

		self.max_distance = max_distance
		self.max_missed_frames = max_missed_frames
		self.next_id = 1
		self.min_dt = min_dt

	def update (self, detections: list[DetectedObject], timestamp: float) -> list[TrackedObject]:
		matched_track_ids = set()
		matched_detection_indices = set()
		current_tracks: list[TrackedObject] = []

		for track in self.tracks:
			best_distance = self.max_distance
			best_detection = None
			best_detection_index = None

			for detection_index, detection in enumerate(detections):
				if detection_index in matched_detection_indices:
					continue
				distance = calc_distance(detection.center, track.current_center)
				if distance < best_distance:
					best_distance = distance
					best_detection = detection
					best_detection_index = detection_index

			if best_detection is not None and best_detection_index is not None:
				track.update(best_detection, timestamp)
				matched_track_ids.add(track.obj_id)
				matched_detection_indices.add(best_detection_index)
				current_tracks.append(track)
			else:
				track.mark_missed()

		for detection_index, detection in enumerate(detections):
			if detection_index in matched_detection_indices:
				continue
			new_track = TrackedObject(self.next_id, detection, timestamp, self.min_dt)
			self.next_id += 1
			current_tracks.append(new_track)
			self.tracks.append(new_track)

		alive_tracks: list[TrackedObject] = []

		for track in self.tracks:
			if not track.should_remove(self.max_missed_frames):
				alive_tracks.append(track)

		self.tracks = alive_tracks
		return current_tracks

