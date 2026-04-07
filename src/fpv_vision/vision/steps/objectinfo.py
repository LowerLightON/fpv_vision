from __future__ import annotations
from fpv_vision.vision.steps.base import BaseStep,Frame
from fpv_vision.vision.steps.detectedobject import DetectedObject
import cv2

class ObjectInfoStep(BaseStep[Frame]):
    def apply(self, frame: Frame) -> Frame:
        contours = frame.get_debug("contours", [])
        objects: list[DetectedObject] = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            area = cv2.contourArea(contour)

            m = cv2.moments(contour)
            if m["m00"] != 0:
                cx = int(m["m10"] / m["m00"])
                cy = int(m["m01"] / m["m00"])
            else:
                cx = x + w // 2
                cy = y + h // 2

            obj = DetectedObject(
                contour = contour,
                bounding_box = (x, y, w, h),
                center = (cx, cy),
                area = area,
            )

            objects.append(obj)
        frame.objects = objects
        return frame




