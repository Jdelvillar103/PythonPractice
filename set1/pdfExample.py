import PyPDF2, os

os.chdir('C:\\Users\\JOsDP23\\OneDrive\\Desktop')

pdfFile = open('meetinfminutes.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages
