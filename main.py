"""
main.py

Entry point for the pdf_parser program. 
Converts a PDF into a database (csv).

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

from pdf_reader import get_images
from ocr_processing import perform_ocr
from text_parser import parse_text
from exporter import export_to_csv



FILE_PATH: str = """.\sample_pdfs\\Neonatologists_USA_1996_Directory[1953].pdf""" 
# """.\sample_pdfs\\Neonatologists_USA_2011_Directory[1954].pdf"""
START_PAGE: int = 11
END_PAGE: int = 11
PATTERN: str = ""

def main() -> None:
    for image in get_images(FILE_PATH, start=START_PAGE, end=END_PAGE + 1):
        text: str = perform_ocr(image)
        parsed_data = parse_text(text)
        export_to_csv(parsed_data)

if __name__ == "__main__":
    main()
