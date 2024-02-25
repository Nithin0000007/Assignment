import pdb
import pytesseract
from PIL import Image
import fitz
import csv,os


# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    for page in doc:
        text += page.get_text()
    return text


def extract_text_from_image(image_file):
    text = pytesseract.image_to_string(Image.open(image_file))
    return text


def extract_key_value_pairs(text):
    key_value_pairs = {}
    lines = text.split('\n')
    # pdb.set_trace()
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            key_value_pairs[key] = value
    return key_value_pairs


def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main(input_file, output_file):
    if input_file.endswith('.pdf'):
        text = extract_text_from_pdf(input_file)
    elif input_file.endswith(('.jpg', '.jpeg', '.png')):
        text = extract_text_from_image(input_file)
    else:
        print("Unsupported file type")
        return

    key_value_pairs = extract_key_value_pairs(text)
    data = [key_value_pairs]
    save_to_csv(data, output_file)
    print(f"Data extracted and saved to {output_file}")


if __name__ == "__main__":
    input_file = "Sample Files/sample2.jpg"
    output_file = "extracted_data.csv"
    main(input_file, output_file)

