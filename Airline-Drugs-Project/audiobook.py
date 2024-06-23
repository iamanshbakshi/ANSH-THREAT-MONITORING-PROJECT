##part2

#reading audio book that is reading pdf

import pyttsx3
from PyPDF2 import PdfFileReader

engine=pyttsx3.init()

reader=PdfFileReader('ansh-bakshi-details.pdf.pdf')

page=reader.getPage(0)

print(page.extractText())

engine.say(page.extractText())

engine.runAndWait()





# import pyttsx3
# from PyPDF2 import PdfFileReader

# engine=pyttsx3.init()

# reader=PdfFileReader('orange-ansh-resumefinal-orange.pdf')

# page=reader.getPage(0)

# print(page.extractText())

# engine.say(page.extractText())

# engine.runAndWait()


 # import PyPDF2
 # import pyttsx3

# Initialize the text-to-speech engine
 # engine = pyttsx3.init()

# Open the PDF file
 # with open('orange-ansh-resumefinal-orange.pdf', 'rb') as file:
    # Create a PDF reader object
     # reader = PyPDF2.PdfFileReader(file)
    
    # Get the first page
     # page = reader.getPage(0)
    
    # Extract text from the first page
     # text = page.extract_text()
    #  print(text)
    
    # Use text-to-speech to read the text
   #   engine.say(text)
 #   engine.runAndWait()

#import PyPDF2
#import pyttsx3

# Initialize the text-to-speech engine
#engine = pyttsx3.init()

# Open the PDF file
#with open('orange-ansh-resumefinal-orange.pdf', 'rb') as file:
    # Create a PDF reader object
    #reader = PyPDF2.PdfFileReader(file)
    
    # Get the first page
    #page = reader.getPage(0)
    
    # Extract text from the first page
    #text = page.extractText()
    #print(text)
    
    # Use text-to-speech to read the text
    #engine.say(text)
    #engine.runAndWait()


