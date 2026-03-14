from fpv_vision.vision.steps.blur import Blur
from fpv_vision.vision.steps.resize import Resize
from fpv_vision.vision.steps.threshold import Threshold
from fpv_vision.vision.steps.morphology import Morphology
from fpv_vision.vision.pipeline.pipeline import Pipeline
from fpv_vision import config as cfg

def build_pipeline()->Pipeline:
    return Pipeline([
        Resize(cfg.CAP["width"], cfg.CAP["height"]),
        Blur(cfg.blur["kernel_size"], cfg.blur["sigma"]),
        Threshold(),
        Morphology(),
    ])
