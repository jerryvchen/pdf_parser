"""
image_processing.py

Contains relevent functions in processing images.

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

import cv2
import numpy as np
from PIL import Image
from typing import Optional


def preprocess_image(image: Image.Image) -> np.ndarray:
    # Convert PIL Image to Numpy array (OpenCV format)
    image: np.ndarray = np.array(image)

    # Convert to Grayscale
    #   Grayscale images are easier to process and analyze since they have only one channel, compared to the three channels in color images.
    gray: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Resize the image
    #   Resizing can help in standardizing the image size for better processing, and it can sometimes help in improving OCR accuracy by resizing to a higher resolution.
    # height: int
    # width: int 
    # height, width = gray.shape
    # new_width: int = 1000
    # new_height: int = int((new_width / width) * height)
    # resized: np.ndarray = cv2.resize(gray, (new_width, new_height))

    # Apply GaussianBlur
    #   This reduces image noise and reduces detail, which can be helpful before thresholding.
    blur: np.ndarray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Adaptive Thresholding
    #   This converts the grayscale image to binary. It is adaptive, meaning the threshold value 
    #   is calculated for smaller regions, yielding different thresholds for different regions. 
    #   This helps in handling varying lighting conditions in different parts of the image.
    thresh: np.ndarray = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2

    )

    # Remove Noise
    #   Morphological operations like opening (erosion followed by dilation) can help in removing small noise in the image.
    # kernel: np.ndarray = np.ones((2, 2), np.uint8)
    # opening: np.ndarray = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # Invert the image
    #   Some OCR engines work better with white text on a black background.
    final: np.ndarray = cv2.bitwise_not(thresh)

    return final