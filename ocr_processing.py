"""
ocr_processing.py

Contains relevent functions in performing OCR.

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

from PIL import Image
from image_processing import preprocess_image
import numpy as np
from pytesseract import pytesseract
from typing import Optional



def perform_ocr(image: Image.Image) -> str:
    processed_image: Optional[np.ndarray] = preprocess_image(image)
    text: str = pytesseract.image_to_string(image)
    return text