"""
pdf_to_img.py

Converts a pdf document to images.

"""
from pathlib import Path
from pdf2image import convert_from_path


PDF_PATH: Path = Path(".\\pdfs\\Neonatologists_USA_1996_Directory[1953].pdf")

images = convert_from_path(PDF_PATH)

for i, image in enumerate(images):
    image.save(f'.\\imgs\\Neonatologists_1996_page_{i+1}.png', 'PNG')
