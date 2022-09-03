from unittest import result
import cv2
import numpy as np

class Sketch:
    def __init__(self) -> None:
        pass
    
    def draw(self, image: np.ndarray) -> np.ndarray:
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inverted = cv2.bitwise_not(grayscale)
        blurred = cv2.GaussianBlur(inverted, (19, 19), sigmaX=0, sigmaY=0)
        resultant = cv2.divide(grayscale, 255 - blurred, scale=256)
        return resultant