import importlib
import os
import PyPDF2

def extract_text_from_pdf(filepath):
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        if reader.isEncrypted:
            reader.decrypt('')  # Provide the password if the PDF is encrypted
        text = ''
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
        return text

# Example usage
filepath = 'data/dexa/dexa_1.pdf'
text_data = extract_text_from_pdf(filepath)
print(text_data)