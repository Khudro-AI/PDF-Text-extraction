from pdf2docx import Converter
import os
def convert_pdf_to_word(pdf_path, word_path):
    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()
input_directory = "../../PDF/tryPDF"

# Replace "pdf_path" with the actual path to your PDF file
for filename in os.listdir(input_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_directory, filename)
        word_path = 'doxConverted2.docx'

convert_pdf_to_word(pdf_path, word_path)
