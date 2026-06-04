from fpv_vision.vision.steps.preprocessing.resize import Resize
from fpv_vision.vision.pipeline.pipeline import Pipeline
from fpv_vision.vision.steps.preprocessing.roi import ROIStep
from fpv_vision.vision.steps.guidance.error import ErrorStep
from fpv_vision.vision.steps.visualization.drawoverlay import DrawOverlayStep
from fpv_vision.vision.steps.utility.time import TimeStep
from fpv_vision.vision.steps.selection.selecttarget import SelectTarget
from fpv_vision.vision.steps.tracking.objecttracking import ObjectTracking
from fpv_vision.vision.steps.visualization.telemetry_overlay import TelemetryOverlayStep
from fpv_vision.core.metricscollector import MetricsCollector
from fpv_vision.vision.steps.detection.objectdetection import ObjectDetection
from fpv_vision.vision.detection.hsv_detector import HSVDetector
from fpv_vision import config as cfg

metrics = MetricsCollector(cfg.HISTORY_SIZE)


def build_preprocessing_steps():
    return [
        TimeStep(),
        Resize(cfg.CAM["WIDTH"], cfg.CAM["HEIGHT"]),
        ROIStep(),
    ]

def build_hsv_detection_steps():
    return [
        ObjectDetection(HSVDetector(
            hsv_lower=cfg.HSV_MASK["LOWER"],
            hsv_upper=cfg.HSV_MASK["UPPER"],
            kernel_size=cfg.MORPH_PARAMS["KERNEL_SIZE"],
            operation=cfg.MORPH_PARAMS["OPERATION"],
            min_area=cfg.FIND_CONTOUR_PARAMS["MIN_AREA"],
            retrieval_mode=cfg.FIND_CONTOUR_PARAMS["RETRIEVAL"],
            approximation_method=cfg.FIND_CONTOUR_PARAMS["APPROXIMATION"]
        ))
    ]

def build_tracking_steps():
    return [
        ObjectTracking(cfg.MAX_DISTANCE, cfg.MAX_MISSED_FRAMES, cfg.MIN_DT),
    ]


def build_visualization_steps():
    return [
        DrawOverlayStep(),
        TelemetryOverlayStep(metrics),
    ]

def build_pipeline() -> Pipeline:
    return Pipeline(
        metrics_collector=metrics,
        steps=[
            *build_preprocessing_steps(),
            *build_hsv_detection_steps(),
            *build_tracking_steps(),
            SelectTarget(),
            ErrorStep(),
            *build_visualization_steps(),
        ],
    )
