"""
main.py

Entry point for the pdf_parser program. 
Converts a PDF into a database (csv).

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

from pdf_reader import get_pages
from ocr_processing import perform_ocr
from text_parser import parse_text
from exporter import export_to_csv



FILE_PATH: str = ".\sample_pdfs\Neonatologists_USA_1996_Directory[1953].pdf" # path to the PDF file
START_PAGE: int = 11
END_PAGE: int = 11

def main() -> None:
    for page in get_pages(FILE_PATH, start = START_PAGE, end = END_PAGE):
        pass

if __name__ == "__main__":
    main()
