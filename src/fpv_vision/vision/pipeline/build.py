from fpv_vision.vision.steps.resize import Resize
from fpv_vision.vision.steps.morphology import Morphology
from fpv_vision.vision.pipeline.pipeline import Pipeline
from fpv_vision.vision.steps.contours import ContoursStep
from fpv_vision.vision.steps.hsvmask import HSVMaskStep
from fpv_vision.vision.steps.roi import ROIStep
from fpv_vision import config as cfg



def build_pipeline()->Pipeline:
    return Pipeline([
        Resize(cfg.CAP["WIDTH"], cfg.CAP["HEIGHT"]),
        ROIStep(),
        HSVMaskStep(cfg.HSV_MASK["LOWER"], cfg.HSV_MASK["UPPER"]),
        Morphology(cfg.MORPH_PARAMS["KERNEL_SIZE"], cfg.MORPH_PARAMS["OPERATION"]),
        ContoursStep(cfg.FIND_CONTOUR_PARAMS["MIN_AREA"],
                     cfg.FIND_CONTOUR_PARAMS["RETRIEVAL"],
                     cfg.FIND_CONTOUR_PARAMS["APPROXIMATION"]),
    ])


#Theshold
#Grayscale(cfg.CVTCOLOR["COLOR"]),
#Blur(cfg.blur["KERNEL_SIZE"], cfg.blur["SIGMA"]),
#Threshold(cfg.threshold["THRESHOLD"],cfg.threshold["MAX_VALUE"] , cfg.threshold["TYPE"]),