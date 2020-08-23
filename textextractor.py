sentences = []
words = []

#Name and location of the image
fileDir='c:\Awesome.png'
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def extract(x):
    #splits the sentence into individual words
    x = (pytesseract.image_to_string(fileDir)).split()
    #Adds the sentence to the list as a whole sentence
    sentences.append(pytesseract.image_to_string(fileDir))
    return x

  
words = extract(fileDir)

#print(pytesseract.image_to_string(fileDir))

#prints a whole sentence
print (sentences[0])

#prints individual words
print(words[0])
