from collections import deque
class MetricsCollector:
    def __init__(self):
        self.step_timings: dict[str, deque[float]] = {}
        self.frame_latencies: deque[float] = deque(maxlen=120)
    def record_step (self, name_step: str, duration_ms: float)->None:
        if name_step not in self.step_timings:
            self.step_timings[name_step] = deque(maxlen=120)
        self.step_timings[name_step].append(duration_ms) 

    def record_frame (self, total_latency_ms: float)->None:
        self.frame_latencies.append(total_latency_ms)
    
    def get_snapshot(self)->dict:
        pass
