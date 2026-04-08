from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class DrawOverlayStep(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        obj = frame.primary_object
        if obj is None:
            if frame.frame_center is not None:
                cv2.circle(frame.image, frame.frame_center, 5, (255, 0, 0), -1)
            return frame

        if obj.smoothed_center is not None:
            cv2.circle(frame.image, obj.smoothed_center, 5, (0, 0, 255), -1)

        if frame.frame_center is not None:
            cv2.circle(frame.image, frame.frame_center, 5, (255, 0, 0), -1)

        if frame.frame_center is not None and obj.smoothed_center is not None:
            cv2.line(frame.image, frame.frame_center, obj.smoothed_center, (255, 255, 0), 2)

        if obj.bounding_box is not None:
            x, y, w, h = obj.bounding_box
            cv2.rectangle(frame.image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if obj.predicted_center is not None:
            cv2.circle(frame.image, obj.predicted_center, 5, (0, 255, 255), -1)

        if obj.velocity is not None:
            vx, vy = obj.velocity
            text = f"vx = {vx:.2f}, vy = {vy:.2f}"
            if obj.angle is not None:
                text += f", angle = {obj.angle:.2f}"
                if obj.obj_id is not None:
                    text += f", obj_id = {obj.obj_id}"
            cv2.putText(frame.image,
                        text,
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2)

        return frame