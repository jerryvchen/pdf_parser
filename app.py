import sys

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                               QVBoxLayout, QLabel, QFileDialog, QSpinBox, 
                               QGroupBox, QFormLayout, QLineEdit, 
                               QPlainTextEdit, QPushButton)

class PDF_Parser_App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PDF Parser")
        self.setGeometry(100, 100, 1280, 720)

        main_widget: QWidget = QWidget()
        self.setCentralWidget(main_widget)

        layout: QHBoxLayout = QHBoxLayout()


        ### COLUMN 1: PDF Selection
        col1_group: QGroupBox = QGroupBox("PDF Selection")
        col1_layout: QVBoxLayout = QVBoxLayout()

        self.pdf_label: QLabel = QLabel("Preview Image")
        col1_layout.addWidget(self.pdf_label)
        self.test_button = QPushButton("test")
        col1_layout.addWidget(self.test_button)

        # self.select_pdf_button: QPushButton = QPushButton("Select PDF")

        col1_group.setLayout(col1_layout)
        



        ### COLUMN 2: Fields and Pattern Matching
        col2_group = QGroupBox("Fields and Pattern Matching")
        col2_layout: QVBoxLayout = QVBoxLayout()

        self.test_button2 = QPushButton("test2")
        col2_layout.addWidget(self.test_button2)

        col2_group.setLayout(col2_layout)

        ### COLUMN 3: Output Settings
        col3_group: QGroupBox = QGroupBox("Ouput Settings")
        col3_layout: QVBoxLayout = QVBoxLayout()

        col3_group.setLayout(col3_layout)



        # Put everything into the main_widget
        layout.addWidget(col1_group)
        layout.addWidget(col2_group)
        layout.addWidget(col3_group)
        main_widget.setLayout(layout)
    
    def select_self(self):
        options: QFileDialog = QFileDialog.options()
        options |= QFileDialog.ReadOnly


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: PDF_Parser_App = PDF_Parser_App()
    window.show()
    sys.exit(app.exec())
