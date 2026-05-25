from collections import deque
class MetricsCollector:
    def __init__(self, history_size: int):
        self.step_timings: dict[str, deque[float]] = {}
        self.frame_latencies: deque[float] = deque(maxlen=history_size)
        self.history_size = history_size

    def record_step (self, name_step: str, duration_ms: float)->None:
        if name_step not in self.step_timings:
            self.step_timings[name_step] = deque(maxlen=self.history_size)
        self.step_timings[name_step].append(duration_ms) 

    def record_frame (self, total_latency_ms: float)->None:
        self.frame_latencies.append(total_latency_ms)
    
    def get_snapshot(self)->dict:
        if not self.frame_latencies:
              frame_last = 0.0
              frame_avg = 0.0
        else:
            frame_last = self.frame_latencies[-1]
            frame_avg = sum(self.frame_latencies) / len(self.frame_latencies)
        if frame_last > 0:
            frame_fps = 1000.0 / frame_last
        else:
            frame_fps = 0.0
        frame_spike = frame_last > 0 and frame_last > frame_avg * 2

        step_snapshot = {}

        for step_name, timings in self.step_timings.items():
            step_last = timings[-1]
            step_avg = sum(timings) / len(timings)

            step_snapshot[step_name] = {
                "last" : step_last,
                "avg" : step_avg
            }

        return {
            "frame_latency": {
                "last" : frame_last,
                "avg" : frame_avg
            },
            "fps" : frame_fps,
            "steps" : step_snapshot,
            "spike" : frame_spike
        }
