import math

def distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.sqrt(dx * dx + dy * dy)