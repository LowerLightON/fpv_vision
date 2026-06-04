from fpv_vision.vision.detection.base_detector import Detector
from fpv_vision.vision.entities.frame import Frame
from fpv_vision.vision.steps.base import BaseStep

class ObjectDetection(BaseStep[Frame]):
    def __init__(self, detector: Detector) -> None:
        self.detector = detector

    def apply(self, frame: Frame) -> Frame:
        detections = self.detector.detect(frame)
        frame.detections = detections
        return frame