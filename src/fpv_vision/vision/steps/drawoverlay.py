from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class DrawOverlayStep(BaseStep):
    def apply(self, frame: Frame) -> Frame:
        if frame.get("smoothed_target_center") is not None:
            cv2.circle(frame.image, frame.get("smoothed_target_center"), 5, (0, 0, 255), -1)

        if frame.get("frame_center") is not None:
            cv2.circle(frame.image, frame.get("frame_center"), 5, (255, 0, 0), -1)

        if frame.get("frame_center") is not None and frame.get("smoothed_target_center") is not None:
            cv2.line(frame.image, frame.get("frame_center"), frame.get("smoothed_target_center"), (255, 255, 0), 2)

        if frame.get("bounding_box") is not None:
            x, y, w, h = frame.get("bounding_box")
            cv2.rectangle(frame.image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        velocity = frame.get("velocity")
        if velocity is not None:
            vx, vy = velocity
            text = f"vx = {vx:.2f}, vy = {vy:.2f}  angle = {frame.get("angle"):.2f}"
            if frame.get("angle") is not None:
                text += f", angle = {frame.get("angle"):.2f}"
            cv2.putText(frame.image,
                        text,
                        (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2)
        return frame