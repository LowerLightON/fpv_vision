from typing import TypeVar, Generic
import time
from fpv_vision.core.metricscollector import MetricsCollector
from fpv_vision.vision.steps.base import BaseStep

T = TypeVar('T')

class Pipeline(Generic[T]):
    def __init__(self, steps: list[BaseStep[T]], metrics_collector: MetricsCollector):
        self.metrics_collector: MetricsCollector = metrics_collector
        self.steps = steps
    def __call__(self, current: T) -> T:
        return self.process(current)
    def process(self, frame: T) -> T:
        if frame is None:
            raise ValueError("Frame is None")
        current = frame
        for step in self.steps:
            start = time.perf_counter()
            current = step(current)
            end = time.perf_counter()
            duration_ms = (end - start) * 1000
            self.metrics_collector.record_step(step.name, duration_ms)
            print(self.metrics_collector.get_snapshot())
        return current
