from fpv_vision.vision.steps.blur import Blur
from fpv_vision.vision.steps.resize import Resize
from fpv_vision.vision.steps.threshold import Threshold
from fpv_vision.vision.steps.morphology import Morphology
from fpv_vision.vision.pipeline.pipeline import Pipeline

def build_pipeline()->Pipeline:
    return Pipeline([
        Resize(),
        Blur(),
        Threshold(),
        Morphology(),
    ])
