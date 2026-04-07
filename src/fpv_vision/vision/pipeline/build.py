from fpv_vision.vision.steps.resize import Resize
from fpv_vision.vision.steps.morphology import Morphology
from fpv_vision.vision.pipeline.pipeline import Pipeline
from fpv_vision.vision.steps.contours import ContoursStep
from fpv_vision.vision.steps.hsvmask import HSVMaskStep
from fpv_vision.vision.steps.roi import ROIStep
from fpv_vision.vision.steps.smoothcenter import SmoothCenter
from fpv_vision.vision.steps.error import ErrorStep
from fpv_vision.vision.steps.drawoverlay import DrawOverlayStep
from fpv_vision.vision.steps.time import TimeStep
from fpv_vision.vision.steps.velocity import VelocityStep
from fpv_vision.vision.steps.prediction import PredictionStep
from fpv_vision.vision.steps.objectinfo import ObjectInfoStep
from fpv_vision.vision.steps.selectprimaryobject import SelectPrimaryObject
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
        SelectPrimaryObject(),
        SmoothCenter(cfg.ALPHA_SMOOTH),
        VelocityStep(cfg.ALPHA_VELOCITY),
        PredictionStep(cfg.PREDICTED_TIME),
        ErrorStep(),
        DrawOverlayStep(),
    ])
