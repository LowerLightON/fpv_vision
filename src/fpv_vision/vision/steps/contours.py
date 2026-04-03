import cv2
from fpv_vision.vision.steps.base import BaseStep
from vision.steps.base import Frame


class ContoursStep(BaseStep):
    def __init__(self, min_area : float, retrieval_mode: int, approximation_method: int) -> None:
        self.min_area = min_area
        self.retrieval_mode = retrieval_mode
        self.approximation_method = approximation_method
        self.prev_center = None
    def apply(self, frame : Frame) ->Frame:
        if frame is None:
            raise ValueError('frame is None')
        if len(frame.image.shape) != 2:
            raise ValueError("ContoursStep expects grayscale/binary image")
        contours, _ = cv2.findContours(frame.image, self.retrieval_mode,self.approximation_method)
        if not contours:
            self.prev_center = None
            frame.image = cv2.cvtColor(frame.image, cv2.COLOR_GRAY2BGR)
            return frame
        frame.image = cv2.cvtColor(frame.image, cv2.COLOR_GRAY2BGR)

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
            return frame

        x, y, w, h = cv2.boundingRect(biggest_contour)

        m = cv2.moments(biggest_contour)
        if m["m00"] != 0:
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
        else:
            cx = x + w // 2
            cy = y + h // 2

        cv2.rectangle(frame.image, (x, y), (x + w, y + h), (0, 255, 0), 2)


        print(f"Target: area={biggest_area}, center=({cx}, {cy})")

        height, width = (frame.image.shape[:2])

        frame_center_x = width // 2
        frame_center_y = height // 2
        if self.prev_center is None:
            self.prev_center = (cx, cy)
        else:
            smooth_x = int(self.prev_center[0] * 0.8 + cx * 0.2)
            smooth_y = int(self.prev_center[1] * 0.8 + cy * 0.2)
            self.prev_center = (smooth_x, smooth_y)
        draw_x, draw_y = self.prev_center
        error_x = (draw_x - frame_center_x)
        error_y = (draw_y - frame_center_y)

        cv2.circle(frame.image, (draw_x, draw_y), 5, (0, 0, 255), -1)
        cv2.circle(frame.image, (frame_center_x, frame_center_y), 5, (255, 0, 0), -1)
        cv2.line(frame.image, (frame_center_x, frame_center_y), (draw_x, draw_y), (255, 255, 0), 2)

        print(f"error_x={error_x}, error_y={error_y}")
        return frame
