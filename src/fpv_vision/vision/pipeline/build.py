from fpv_vision.vision.steps.blur import Blur
from fpv_vision.vision.steps.resize import Resize
from fpv_vision.vision.steps.threshold import Threshold
from fpv_vision.vision.steps.morphology import Morphology
from fpv_vision.vision.pipeline.pipeline import Pipeline
from fpv_vision.vision.steps.gray import Gray
from fpv_vision import config as cfg

def build_pipeline()->Pipeline:
    return Pipeline([
        Resize(cfg.CAP["WIDTH"], cfg.CAP["HEIGHT"]),
        Gray(cfg.CVTCOLOR["COLOR"]),
        Blur(cfg.blur["KERNEL_SIZE"], cfg.blur["SIGMA"]),
        Threshold(cfg.threshold["THRESHOLD"],cfg.threshold["MAX_VALUE"] , cfg.threshold["TYPE"]),
        Morphology(),
    ])
