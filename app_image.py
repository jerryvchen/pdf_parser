from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel
from pdf2image import convert_from_path

from pathlib import PurePath
from PIL import Image


def pdf_preview(label: QLabel, file_path: PurePath, page: int = 1) -> None:
    """
    Converts a QLabel to show a picture instead. 

    :param file_path: Path to the PDF.
    :type file_path: pathlib.PurePath
    :param page: The page which should be rendered, 1-indexed
    :type: int
    :return: A QLabel object containing the image
    :rtype: PySide.QtWidgets.QLabel
    """

    try:
        # Converts the first page of the PDF to an image
        image: Image.Image = convert_from_path(file_path, first_page=page, last_page=page)[0]

        # Convert the PIL image to a Qt-compatible QImage
        q_image: QImage = QImage(image.tobytes(), image.width, image.height, QImage.Format.Format_RGB888)

        # Calculated the scaled size to fit the label while maintaining aspect ratio
        label_width: QSize = label.size().width()
        q_image = q_image.scaledToWidth(label_width)

        # Convert the QImage to a QPixmap
        pixmap: QPixmap = QPixmap.fromImage(q_image)

        # Add the QPixmap to the QLabel
        label.setPixmap(pixmap)
        label.setScaledContents(False)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    except Exception as e:
        print(f"Error loading PDF: {e}")

