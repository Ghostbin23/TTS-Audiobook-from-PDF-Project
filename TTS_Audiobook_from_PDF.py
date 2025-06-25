import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename() # asks to open a file's name
pdfreader = PyPDF2.PdfReader(book) # assigns an object, a pdf reader
pages = len(pdfreader.pages) # returns number of pages in the pdf

# we now need to read all data in PDF pages

for num in range(0,pages): # iterate through each page
    page = pdfreader.pages[num] # gets the page at the number 'num', returned as an object
    text = page.extract_text() # extracts plaintext of the page
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()