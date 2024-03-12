import pytesseract
import os
from PIL import Image
from pdf2image import convert_from_path
#from docx import Document
import re

def extract_text_from_image(img_path, confidence_threshold=80):
    result = pytesseract.image_to_data(img_path, lang='ben', output_type=pytesseract.Output.DICT)
    extracted_text = " ".join(word_text for i, word_text in enumerate(result['text']) if int(result['conf'][i]) >= confidence_threshold)
    return extracted_text

def clean_text(bangla_text):
    ##bangla_text = re.sub(r'[^a-zA-Z0-9\s]', '', bangla_text) #For english Pdf
    #bangla_text = re.sub(r'[^\u0980-\u09FF\s]', '', bangla_text) #Remove special Characters
    #bangla_text = re.sub(r'^\s*\d+\s*$', '', bangla_text, flags=re.MULTILINE) #Remove page numbers
    ##bangla_text = re.sub(r'\b\d+\b', '', bangla_text)  # Remove all numbers
    #bangla_text = re.sub(r'\n\s*\n', '\n', bangla_text)  # Remove empty lines
    ##bangla_text = re.sub(r'\[[^\]]+\]', '', bangla_text)  # Remove text in brackets (assuming headers)
    #bangla_text = re.sub(r'\s+', ' ', bangla_text).strip()  # Remove extra spaces
    ##bangla_text = re.sub(r'\[[^\]]+\]$', '', bangla_text, flags=re.MULTILINE)  # Remove footer (assuming footer is in brackets at the end of pages)
    return bangla_text

def process_pdf(input_directory, filename, confidence_threshold=80):
    #doc = Document()
    file = open(f"{filename}.txt", "w")
    pdf_path = os.path.join(input_directory, filename)
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        
        img_path = os.path.join(input_directory, f'{i+1}.png')
        image.save(img_path, 'PNG')

        text = extract_text_from_image(img_path, confidence_threshold)
        cleaned_text = clean_text(text)
        
        #doc.add_paragraph(cleaned_text)
        file.write(cleaned_text)
        file.write("\n")
        os.remove(img_path)

        print(f"Page {i + 1} processed.")

    #doc_path = os.path.join(input_directory, f'{filename}.docx')
    #doc.save(doc_path)
    file_path = os.path.join(input_directory, f'{filename}.docx')
    file.close() 
    print(f"Document saved to {file_path}.")

def main():
    input_directory = "."
    confidence_threshold = 80 
    skip_first_page = True

    for root, _, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".pdf"):
                process_pdf(root, filename, confidence_threshold)

if __name__ == "__main__":
    main()