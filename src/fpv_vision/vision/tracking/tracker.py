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
		matched_detection_indices = set()
		current_tracks: list[TrackedObject] = []
		candidates: list[tuple[float, TrackedObject, DetectedObject, int]] = []

		for track in self.tracks:

			dt = timestamp - track.last_timestamp
			track.predict(dt)

			for detection_index, detection in enumerate(detections):
				if detection_index in matched_detection_indices:
					continue

				matching_center = self._get_matching_center(track)
				distance = calc_distance(matching_center, detection.center)

				if distance < self.max_distance:
					candidates.append((distance, track, detection, detection_index))
				
		candidates.sort(key=lambda item: item[0])

		matched_tracks = set()
		matched_detection_indices = set()

		for distance, track, detection, detection_index in candidates:
			if track.obj_id in matched_tracks or detection_index in matched_detection_indices:
				continue
			else:
				track.update(detection, timestamp)
				matched_tracks.add(track.obj_id)
				matched_detection_indices.add(detection_index)
				current_tracks.append(track)
		
		for track in self.tracks:
			if track.obj_id not in matched_tracks:
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
		return self.tracks
	
	def _get_matching_center(self, track: TrackedObject) -> tuple[float, float]:
		if track.predicted_center is not None:
			return track.predicted_center
		else:
			return track.current_center
