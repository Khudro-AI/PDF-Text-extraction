# PDF text Extraction Pipeline:
---

Here you will be able to find few approaches we have tried to ensure the best quality of the extracted text from pdf.

Here you will be able to find codebase with pdfminer, pypdf2, pdfplumber and so on. Among all of them the pytesseract resulted the best.

- **pytesseract** is an ocr method. Means to use this tool We 1st converted the pdf pages from pdf to images. Then extracted bangla text from that image. We used **regix** to clean text.

to run the tool **pytesseract** follow these steps:
1. Clone repo, `cd pdf_text_extraction` , open terminal, write `pip install -r requirements.txt`
2. Open **text_extraction.py** file. Go to line 61 and change the location path of your input pdf. 
3. Go to line **9** and change the value of lang. For bangla `lang="ben"` for english `lang="en"` for both `lang="en+ben"` 
3. Go to terminal run the **text_extraction.py** file.

in case of any error you may also need to 
```
Run the bash command `sudo apt install tesseract-ocr`. 
    To install Bangla dataset run: `sudo apt-get install tesseract-ocr-ben` 
    To add location: `export TESSDATA_PREFIX=/usr/share/tesseract-ocr/{version}/`
    For example if version is 5.1.1 then in {vertion} section write `5`
    To check version: `tesseract --version`
```
