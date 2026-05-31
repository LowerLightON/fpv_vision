from fpv_vision.vision.source.base_source_frame import FrameSource
from fpv_vision.vision.entities.frame import Frame
import cv2
import time

class VideoFileSource(FrameSource):
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path
        self._cap: cv2.VideoCapture | None = None
    
    def open(self) -> None:
        if self._cap is not None:
            return
        cap = cv2.VideoCapture(str(self.video_path))
        if not cap.isOpened():
            raise RuntimeError(f"Could not open video file: {self.video_path}")
        self._cap = cap

    def read(self) -> Frame | None:
        if self._cap is None:
            raise RuntimeError("Video file is not opened. Call open() first.")
        ret, img = self._cap.read()    
        if not ret:
            return None
        timestamp = time.perf_counter()
        frame = Frame(img, timestamp)
        return frame
    
    def close(self) -> None:
        if self._cap is not None:
            self._cap.release()
            self._cap = None