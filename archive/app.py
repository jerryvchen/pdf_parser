"""
app.py

Contains the GUI for the PDF Parser Project.
"""

import sys

from pathlib import PurePath
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                               QVBoxLayout, QLabel, QFileDialog, QSpinBox, 
                               QGroupBox, QFormLayout, QLineEdit, 
                               QPlainTextEdit, QPushButton)

from app_image import pdf_preview

class PDF_Parser_App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PDF Parser")
        self.setGeometry(100, 100, 1280, 720)

        main_widget: QWidget = QWidget()
        self.setCentralWidget(main_widget)

        layout: QHBoxLayout = QHBoxLayout()

        # Variables
        self.file_path: PurePath | None = None
        self.start_page: int = 1
        self.end_page: int = 1


        ### COLUMN 1: PDF Selection
        col1_group: QGroupBox = QGroupBox("PDF Selection")
        col1_layout: QVBoxLayout = QVBoxLayout()

        # Select PDF
        self.file_path_title_label: QLabel = QLabel("Selected File: ", self)
        col1_layout.addWidget(self.file_path_title_label)
        self.file_path_label: QLabel = QLabel("[No File Selected]")
        col1_layout.addWidget(self.file_path_label)
        self.select_pdf_button: QPushButton = QPushButton("Select PDF")
        self.select_pdf_button.clicked.connect(self.select_pdf)
        col1_layout.addWidget(self.select_pdf_button)

        col1_layout.addStretch()

        # PDF Preview
        self.pdf_preview_title: QLabel = QLabel("Preview of Start Page: ")
        col1_layout.addWidget(self.pdf_preview_title)
        self.pdf_preview: QLabel = QLabel("[No File Selected]")
        self.pdf_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        col1_layout.addWidget(self.pdf_preview)

        col1_layout.addStretch()

        # Start and End Page #'s 
        self.page_range_group: QGroupBox = QGroupBox()
        self.page_range_layout: QHBoxLayout = QHBoxLayout()

        self.start_page_group: QGroupBox = QGroupBox()
        self.start_page_layout: QVBoxLayout = QVBoxLayout()
        start_page_title: QLabel = QLabel("Start Page: ")
        self.start_page_layout.addWidget(start_page_title)
        self.start_page_input: QLineEdit = QLineEdit(self)
        self.start_page_layout.addWidget(self.start_page_input)
        self.start_page_group.setLayout(self.start_page_layout)
        self.page_range_layout.addWidget(self.start_page_group)

        self.page_range_layout.addStretch()

        self.end_page_group: QGroupBox = QGroupBox()
        self.end_page_layout: QVBoxLayout = QVBoxLayout()
        end_page_title: QLabel = QLabel("End Page: ")
        self.end_page_layout.addWidget(end_page_title)
        self.end_page_input: QLineEdit = QLineEdit(self)
        self.end_page_layout.addWidget(self.end_page_input)
        self.end_page_group.setLayout(self.end_page_layout)
        self.page_range_layout.addWidget(self.end_page_group)
        
        self.page_range_group.setLayout(self.page_range_layout)
        col1_layout.addWidget(self.page_range_group)


        col1_group.setLayout(col1_layout)

        

        ### COLUMN 2: Fields and Pattern Matching
        col2_group: QGroupBox = QGroupBox("Fields and Pattern Matching")
        col2_layout: QVBoxLayout = QVBoxLayout()

        self.test_button2 = QPushButton("test2")
        col2_layout.addWidget(self.test_button2)

        col2_group.setLayout(col2_layout)



        ### COLUMN 3: Output Settings
        col3_group: QGroupBox = QGroupBox("Ouput Settings")
        col3_layout: QVBoxLayout = QVBoxLayout()

        col3_group.setLayout(col3_layout)


        col1_group.setMaximumWidth(self.width() // 3)
        col2_group.setMaximumWidth(self.width() // 3)
        col3_group.setMaximumWidth(self.width() // 3)
        layout.addWidget(col1_group)
        layout.addWidget(col2_group)
        layout.addWidget(col3_group)
        main_widget.setLayout(layout)
    
    def select_pdf(self) -> None:
        options: QFileDialog = QFileDialog.Options()    
        options |= QFileDialog.ReadOnly
        pdf_file, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF files (*.pdf);;All Files (*)", options=options)
        
        if pdf_file:
            self.file_path = PurePath(pdf_file)
            self.file_path_label.setText(f"{self.file_path}")
            pdf_preview(self.pdf_preview, self.file_path)

            # Edit page ranges


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: PDF_Parser_App = PDF_Parser_App()
    window.show()
    sys.exit(app.exec())
