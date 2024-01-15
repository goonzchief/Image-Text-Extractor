from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)

            print("Extracted Text:")
            print(text)

    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    image_path = "path/to/your/image.png"
    extract_text_from_image(image_path)
