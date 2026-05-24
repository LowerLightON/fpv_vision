from fpv_vision.vision.steps.base import BaseStep
from fpv_vision.vision.entities.frame import Frame
from fpv_vision.core.metricscollector import MetricsCollector
import cv2

class TelemetryOverlayStep(BaseStep[Frame]):
    def __init__(self, metricscollector: MetricsCollector ) -> None:
        self.metricscollector = metricscollector
    
    def apply(self, frame: Frame) -> Frame:
        snapshot = self.metricscollector.get_snapshot()

        latency = snapshot["frame_latency"]["last"]
        frame_fps = snapshot["fps"]

        cv2.putText(
            frame.image,
            f"Latency: {latency:.2f} ms",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame.image,
            f"FPS: {frame_fps:.2f}",
            (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

        return frame