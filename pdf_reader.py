"""
pdf_reader.py

Contains functions that relate to reading the PDF.

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

import pdfplumber
from pdfplumber.page import Page
from pathlib import Path
from typing import Iterator

def get_pages(file_path: Path, start: int = 0, end: int = None) -> Iterator[Page]:
    """
    Continually yields pages given the PDF path and the start and end page (inclusive).

    :param file_path: Path to the PDF file.
    :type file_path: pathlib.Path
    :param start: Start page (inclusive).
    :type start: int
    :param end: End page (inclusive).
    :type end: int
    :return: Continually yields pdfplumber.page.Page if possible
    :rtype: pdfplumber.page.Page
    """
    with pdfplumber.open(file_path) as pdf:
        if start > 0:
            start -= 1 # inclusive range
        if end is None:
            end = len(pdf.pages)

        
        for i in range(start, end):
            yield pdf.pages[i]