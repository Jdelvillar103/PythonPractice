import docx

def getText(filename):
    document = docx.Document(filename)
    fullText = []
    for para in document.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
    

print(getText('C:\\Users\\JOsDP23\\OneDrive\\Desktop\\demo.docx'))