import cv2
import numpy as np
from fpv_vision.vision.steps.base import BaseStep

class ContoursStep(BaseStep):
    def __init__(self, min_area : float, retrieval_mode: int, approximation_method: int) -> None:
        self.min_area = min_area
        self.retrieval_mode = retrieval_mode
        self.approximation_method = approximation_method
    def apply(self, frame : np.ndarray) -> np.ndarray:
        if frame is None:
            raise ValueError('frame is None')
        if len(frame.shape) != 2:
            raise ValueError("ContoursStep expects grayscale/binary image")
        contours, _ = cv2.findContours(frame, self.retrieval_mode,self.approximation_method)
        if not contours:
            return cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        result = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        biggest_contour = None
        biggest_area = 0.0

        for contour in contours:
            area = cv2.contourArea(contour)

            if area < self.min_area:
                continue

            if area > biggest_area:
                biggest_area = area
                biggest_contour = contour

        if biggest_contour is None:
            return result

        x, y, w, h = cv2.boundingRect(biggest_contour)

        M = cv2.moments(biggest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx = x + w // 2
            cy = y + h // 2

        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(result, (cx, cy), 5, (0, 0, 255), -1)

        print(f"Target: area={biggest_area}, center=({cx}, {cy})")

        height, width = frame.shape[:2]

        frame_center_x = width // 2
        frame_center_y = height // 2

        error_x = cx - frame_center_x
        error_y = cy - frame_center_y

        cv2.circle(result, (frame_center_x, frame_center_y), 5, (255, 0, 0), -1)
        cv2.line(result, (frame_center_x, frame_center_y), (cx, cy), (255, 255, 0), 2)

        print(f"error_x={error_x}, error_y={error_y}")
        return result
