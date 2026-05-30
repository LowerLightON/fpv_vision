import math

def distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.sqrt(dx * dx + dy * dy)

def iou(bbox_a: tuple[int, int, int, int], bbox_b: tuple[int, int, int, int]) -> float:
    ax, ay, aw, ah = bbox_a
    bx, by, bw, bh = bbox_b
    
    a_right = ax + aw
    a_bottom = ay + ah
    b_right = bx + bw
    b_bottom = by + bh

    inter_left = max(ax, bx)
    inter_top = max(ay, by)
    inter_right = min(a_right, b_right)
    inter_bottom = min(a_bottom, b_bottom)

    inter_width = max(0, inter_right - inter_left)
    inter_height = max(0, inter_bottom - inter_top)
    inter_area = inter_width * inter_height
    area_a = aw * ah
    area_b = bw * bh
    union_area = area_a + area_b - inter_area

    iou = inter_area / union_area if union_area > 0 else 0.0
    return iou