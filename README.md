# Image Text Extractor

## Overview

The Image Text Extractor is a Python script designed to simplify the extraction of text content from images using Optical Character Recognition (OCR). It leverages the Tesseract OCR engine through the `pytesseract` library, making it a user-friendly tool for integrating OCR capabilities into various applications.

## Requirements

Before running the script, ensure that you have the following dependencies installed:

- **Tesseract OCR:** [Download Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- **Python 3.x**
- **`pytesseract` Python Library:** Install it using `pip install pytesseract`

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/image-text-extractor.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd image-text-extractor
    ```

3. **Run the script:**

    ```bash
    python extract_text.py path/to/your/image.png
    ```

    Replace `path/to/your/image.png` with the actual path to your image file.

## Example

Suppose you have an image named `example_image.png`. To extract text from this image, run the following command:

```bash
python extract_text.py example_image.png
