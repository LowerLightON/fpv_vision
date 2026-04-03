import cv2
import numpy as np

from fpv_vision.vision.steps.base import BaseStep, Frame

class HSVMaskStep(BaseStep):
    def __init__(self, lower: tuple, upper: tuple)->None:
        self.lower = np.array(lower, dtype=np.uint8)
        self.upper = np.array(upper, dtype=np.uint8)
    def apply(self, frame: Frame) -> Frame:
        if frame.image is None:
            raise ValueError('Frame is None')
        original = frame.image.copy()
        frame.image = cv2.cvtColor(frame.image, cv2.COLOR_BGR2HSV)
        frame.image = cv2.inRange(frame.image, self.lower, self.upper)
        result = cv2.bitwise_and(original, original, mask=frame.image)
        cv2.imshow("mask", frame.image)
        cv2.imshow('result', result)
        return frame


