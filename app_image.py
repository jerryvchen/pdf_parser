from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel
from pdf2image import convert_from_path

from pathlib import PurePath
from PIL import Image


def pdf_preview(file_path: PurePath, page: int = 1) -> QLabel:
    preview_label: QLabel = QLabel()

    try:
        # Converts the first page of the PDF to an image
        image: Image.Image = convert_from_path(file_path, first_page=page, last_page=page)[0]

        # Convert the PIL image to a Qt-compatible QImage
        q_image: QImage = QImage(image.tobytes(), image.width, image.height, QImage.Format.Format_RGB888)

        # Convert the QImage to a QPixmap
        pixmap: QPixmap = QPixmap.fromImage(q_image)

        # Add the QPixmap to the QLabel
        preview_label.setPixmap(pixmap)
        preview_label.setScaledContents(True) # Scale the image to fit the label
    
    except Exception as e:
        print(f"Error loading PDF: {e}")




    return preview_label

