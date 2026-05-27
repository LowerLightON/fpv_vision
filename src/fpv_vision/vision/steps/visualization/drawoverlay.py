from fpv_vision.vision.steps.base import BaseStep
from fpv_vision.vision.entities.frame import Frame
from fpv_vision.vision.tracking.tracked_object import TrackedObject
import cv2

class DrawOverlayStep(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        obj = frame.selected_target

        if obj is None:
            if frame.frame_center is not None:
                cv2.circle(frame.image, frame.frame_center, 5, (255, 0, 0), -1)
            return frame
        
        color = self._get_track_color(obj)

        if obj.current_center is not None:
            cv2.circle(frame.image, obj.current_center, 5, color, -1)

        if frame.frame_center is not None:
            cv2.circle(frame.image, frame.frame_center, 5, (255, 0, 0), -1)

        if frame.frame_center is not None and obj.current_center is not None:
            cv2.line(frame.image, frame.frame_center, obj.current_center, color, 2)

        bbox = obj.current_detection.bounding_box
        if bbox is not None:
            x, y, w, h = bbox
            cv2.rectangle(frame.image, (x, y), (x + w, y + h), color, 2)

            if obj.obj_id is not None:
                text_y = y - 10 if y - 10 > 10 else y + 20
                cv2.putText(
                    frame.image,
                    f"id: {obj.obj_id}",
                    (x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    color,
                    2
                )
        
        if obj.predicted_center is not None:
            predicted_x, predicted_y = obj.predicted_center
            predicted_point = int(predicted_x), int(predicted_y)
            cv2.circle(frame.image, predicted_point, 5, (0, 255, 255), -1)

        if obj.velocity is not None:
            vx, vy = obj.velocity
            text = f"vx = {vx:.2f}, vy = {vy:.2f}"
            if obj.angle is not None:
                text += f", angle = {obj.angle:.2f}"
            cv2.putText(frame.image,
                        text,
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        color,
                        2)

        return frame
    
    def _get_track_color(self, track: TrackedObject) -> tuple[int, int, int]:
        if track.is_lost:
            return (0, 255, 255)

        if track.is_new:
            return (255, 0, 0)

        return (0, 255, 0)