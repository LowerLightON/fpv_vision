from fpv_vision.vision.entities.detected_object import DetectedObject
from fpv_vision.vision.entities.frame import Frame
from fpv_vision.vision.detection.base_detector import Detector
import cv2
import numpy as np

class HSVDetector(Detector):
    def __init__(self, 
                 hsv_lower: tuple[int, int, int] | np.ndarray,
                 hsv_upper: tuple[int, int, int] | np.ndarray,
                 kernel_size: int,
                 operation: int,
                 min_area: float,
                 retrieval_mode: int,
                 approximation_method: int,
                 ) -> None:
        self.hsv_lower = np.array(hsv_lower, dtype=np.uint8)
        self.hsv_upper = np.array(hsv_upper, dtype=np.uint8)
        self.kernel_size = kernel_size
        self.operation = operation
        self.min_area = min_area
        self.retrieval_mode = retrieval_mode
        self.approximation_method = approximation_method
    def detect(self, frame: Frame) -> list[DetectedObject]:
        mask = self._create_mask(frame)

        morphology_img = self._apply_morphology(mask)
        frame.set_debug("morphology_image", morphology_img)

        contours = self._find_contours(morphology_img)
        frame.set_debug("contours", contours)
        detections = self._contours_to_detections(contours)
        return detections



    def _create_mask(self, frame: Frame) -> np.ndarray:
        img = cv2.cvtColor(frame.image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(img, self.hsv_lower, self.hsv_upper)
        frame.set_debug("bitwise_image", cv2.bitwise_and(frame.image, frame.image, mask=mask))
        return mask
    
    def _apply_morphology(self, mask: np.ndarray) -> np.ndarray:
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        morphology_img = cv2.morphologyEx(mask, self.operation, kernel)
        return morphology_img
    
    def _find_contours(self, morphology_img: np.ndarray) -> list[np.ndarray]: 
        contours, _ = cv2.findContours(morphology_img, self.retrieval_mode,self.approximation_method)
        valid_contours = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area >= self.min_area:
                valid_contours.append(contour)
        return valid_contours 

    def _contours_to_detections(self, contours: list[np.ndarray]) -> list[DetectedObject]:
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
                bounding_box=(x, y, w, h),
                center=(cx, cy),
                area=area,
                contour=contour,
            )

            objects.append(obj)
        return objects