import pdfquery

def extractFileData(file_path, file_type):
    if file_type == 'PDF':
        return extractPdfFileData(file_path)
    elif file_type == 'jpg' or file_type == 'png':
        return extractImageFileData(file_path)
    else:
        raise Exception('Unknown file type: ' + file_type)
    
def extractPdfFileData(file_path):
    pdf = pdfquery.PDFQuery(file_path)
    pdf.load()
    pdf.tree.write('data.xml', pretty_print = True)
    text_elements = pdf.pq('LTTextLineHorizontal')
    text = [t.text for t in text_elements]
    return text

def extractImageFileData(file_path):
    return Exception('Not implemented yet')


 
   