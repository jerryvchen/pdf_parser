"""
pdf_reader.py

Contains functions that relate to reading the PDF.

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

from pdf2image import convert_from_path
from pathlib import Path
from PIL import Image
from typing import Generator


def get_images(file_path: Path, start: int, end: int) -> Generator[Image.Image, None, None]:
    """
    Continually yields images given the PDF path and the start and end page (inclusive).

    :param file_path: Path to the PDF file.
    :type file_path: pathlib.Path
    :param start: Start page (inclusive).
    :type start: int
    :param end: End page (inclusive).
    :type end: int
    :return: Continually yields pdfplumber.page.Page if possible
    :rtype: PIL.Image.Image
    """
    for i in range(start, end):
        image: Image.Image = convert_from_path(file_path, dpi=300, first_page=i, last_page=i)[0]
        yield image