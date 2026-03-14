import cv2
from fpv_vision import config as cfg
CAP = cfg.CAP

class Camera:
    def __init__(self, device=CAP["device"], width=CAP["width"], height=CAP["height"], fps=CAP["fps"]):
        self.device = device
        self.width = width
        self.height = height
        self.fps = fps
        self._cap = None

    def open(self):
        if self._cap is not None:
            return
        cap = cv2.VideoCapture(self.device, cv2.CAP_V4L2)
        if not cap.isOpened():
            raise RuntimeError("Camera is not opened. Call open() first.")

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        cap.set(cv2.CAP_PROP_FPS, self.fps)

        self._cap = cap
    def read(self):
        if self._cap is None:
            raise RuntimeError("Could not open camera")
        ok, frame = self._cap.read()
        if not ok:
            raise RuntimeError("Could not read frame")
        return frame

    def close(self):
        if self._cap is not None:
            self._cap.release()
            self._cap = None