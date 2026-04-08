import math

def distance(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.sqrt(dx * dx + dy * dy)