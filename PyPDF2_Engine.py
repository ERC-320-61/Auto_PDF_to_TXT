import PyPDF2


'''
This part uses the PyPDF2 to take the content of PDFs and prepare them to be written to text file
'''

Content_Dictionary = {}

pdfFileObject = open(r'PDFs/Resume 2_0.pdf', 'rb')  # Creating PDF File Object to read from
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)     # Creating PDF reader object
pageCount = pdfReader.numPages                      # Collect Page count
for page in range(pageCount):
    pageObject = pdfReader.getPage(page)            # Create a page object for specified page
    Text = pageObject.extractText()                 # Store text from page in variable
    Content_Dictionary[page] = Text                 # Temporarily store page and its content

pdfFileObject.close()                               # Closing PDF File Object

'''
Taking text from pdf and writing it on new textFile
'''
for page in range(len(Content_Dictionary)):                         # Work through dictionary
    NewFile = open(f"ConvertedPDFs/Conversion{page}.txt", "w")      # Make new file for each page
    NewFile.write(Content_Dictionary[page])                         # Write string content to page
    NewFile.close()                                                 # Close File after writing contents of page
