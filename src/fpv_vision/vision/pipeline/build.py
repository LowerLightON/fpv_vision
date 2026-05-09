from vision.steps.preprocessing.resize import Resize
from vision.steps.preprocessing.morphology import Morphology
from fpv_vision.vision.pipeline.pipeline import Pipeline
from vision.steps.detection.contours import ContoursStep
from vision.steps.preprocessing.hsvmask import HSVMaskStep
from vision.steps.preprocessing.roi import ROIStep
from vision.steps.tracking.smoothcenter import SmoothCenter
from vision.steps.guidance.error import ErrorStep
from vision.steps.visualization.drawoverlay import DrawOverlayStep
from vision.utils.time import TimeStep
from vision.steps.legacy.velocity import VelocityStep
from vision.steps.legacy.prediction import PredictionStep
from vision.steps.detection.object_extraction import ObjectInfoStep
from vision.steps.selection.selectprimaryobject import SelectPrimaryObject
from vision.steps.tracking.objecttracking import ObjectTracking
from fpv_vision import config as cfg


def build_pipeline()->Pipeline:
    return Pipeline([
        TimeStep(),
        Resize(cfg.CAP["WIDTH"], cfg.CAP["HEIGHT"]),
        ROIStep(),
        HSVMaskStep(cfg.HSV_MASK["LOWER"], cfg.HSV_MASK["UPPER"]),
        Morphology(cfg.MORPH_PARAMS["KERNEL_SIZE"], cfg.MORPH_PARAMS["OPERATION"]),
        ContoursStep(cfg.FIND_CONTOUR_PARAMS["MIN_AREA"],
                     cfg.FIND_CONTOUR_PARAMS["RETRIEVAL"],
                     cfg.FIND_CONTOUR_PARAMS["APPROXIMATION"]),
        ObjectInfoStep(),
        ObjectTracking(cfg.MAX_DISTANCE, cfg.MAX_MISSED_FRAMES),
        SelectPrimaryObject(),
        SmoothCenter(cfg.ALPHA_SMOOTH),
        VelocityStep(cfg.ALPHA_VELOCITY),
        PredictionStep(cfg.PREDICTED_TIME),
        ErrorStep(),
        DrawOverlayStep(),
    ])
