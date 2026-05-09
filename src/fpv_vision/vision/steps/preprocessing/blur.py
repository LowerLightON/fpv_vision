from fpv_vision.vision.steps.base import BaseStep, Frame
import cv2

class Blur(BaseStep[Frame]):
    def __init__(self, kernel_size: tuple[int, int] , sigma: float) -> None:
        self.kernel_size = kernel_size
        self.sigma = sigma
    def apply(self, frame: Frame) -> Frame:
        if frame.image is None:
            raise ValueError('frame is None')
        frame.image = cv2.GaussianBlur(frame.image, self.kernel_size, self.sigma)
        return frame