import pytesseract
from PIL import Image



def ocr_with_tesseract(image_path):
    # Perform OCR on the image and get the recognized text
    recognized_text = pytesseract.image_to_string(Image.open(image_path))
    print(recognized_text)
    return recognized_text

if __name__ == "__main__":
    # Replace 'your_image_file.png' with the path to your image containing the columns.
    image_path = '.\\imgs\\Neonatologists_1996_page_11.png'

    # Step 1: Perform OCR on the image and get the recognized text
    ocr_text = ocr_with_tesseract(image_path)

