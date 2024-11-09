# **************************************** assignment 8 ****************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/76-Day-76-Exercise-8/.tutorial/Tutorial.md

# pypdf module
# to use pypdf, we need to 1st install it
from pypdf import PdfWriter
# imports PdfWriter class from pypdf module

def PDFmerge(pdfs, outpdf):
    pdfWriter = PdfWriter()#creates pdfWriter obj from PdfWriter()
    for pdf in pdfs:
        pdfWriter.append(pdf)
    # writing combined pdf to output pdf file
    with open(outpdf, 'wb') as f: #wb: write binary 
        pdfWriter.write(f)#with ensures all files are closed properly

pdfs = ["23.pdf", "234.pdf", "2345.pdf"]
outpdf = "combinedPdf.pdf"
PDFmerge(pdfs, outpdf)