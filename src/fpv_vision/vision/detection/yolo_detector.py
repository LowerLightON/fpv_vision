from fpv_vision.vision.detection.base_detector import Detector
from fpv_vision.vision.entities.detected_object import DetectedObject
from fpv_vision.vision.entities.frame import Frame
import onnxruntime as ort
import cv2
import numpy as np

class YoloDetector(Detector):
    def __init__(self, model_path: str, confidence_threshold: float, input_size: int, allowed_class_ids: list[int]) -> None:
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.input_size = input_size
        self.allowed_class_ids = allowed_class_ids

        self.model = self._load_model(self.model_path)

        self.input_name = self.model.get_inputs()[0].name
        self.output_name = self.model.get_outputs()[0].name


    def detect(self, frame: Frame ) -> list[DetectedObject]:
        results = self._run_inference(frame)
        detections = self._results_to_detections(results, frame)
        return detections
    
    def _load_model(self, model_path: str) -> ort.InferenceSession:
        return ort.InferenceSession(model_path)
        
    def _preprocess(self, frame: Frame) -> np.ndarray:
        image = frame.image
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        resized_image = cv2.resize(rgb_image, (self.input_size, self.input_size))
        normalized_image = resized_image.astype(np.float32) / 255.0
        chw_image = np.transpose(normalized_image, (2, 0, 1))
        batched_image = np.expand_dims(chw_image, axis=0)
        return batched_image

    def _run_inference(self, frame: Frame) -> np.ndarray:
        input_tensor = self._preprocess(frame)

        outputs = self.model.run([self.output_name], {self.input_name: input_tensor})

        output = outputs[0]

        if not isinstance(output, np.ndarray):
            raise TypeError("YOLO output must be numpy array")
        
        return output

    def _results_to_detections(self, results: np.ndarray, frame: Frame) -> list[DetectedObject]:
        detections: list[DetectedObject] = []

        predictions = results[0].T

        frame_height, frame_width = frame.image.shape[:2]

        scale_x = frame_width / self.input_size
        scale_y = frame_height / self.input_size

        for prediction in predictions:
            x_center = float(prediction[0]) * scale_x
            y_center = float(prediction[1]) * scale_y
            width = float(prediction[2]) * scale_x
            height = float(prediction[3]) * scale_y

            class_scores = prediction[4:]
            class_id = int(np.argmax(class_scores))

            if class_id not in self.allowed_class_ids:
                continue
            
            confidence = float(class_scores[class_id])

            if confidence < self.confidence_threshold:
                continue

            x = int(x_center - width / 2)
            y = int(y_center - height / 2)
            w = int(width)
            h = int(height)

            detections.append(
                DetectedObject(
                    bounding_box=(x, y, w, h),
                    center=(int(x_center), int(y_center)),
                    area=float(w * h),
                    confidence=confidence,
                    class_id=class_id,
                    label=str(class_id),
                )
            )

        return detections
