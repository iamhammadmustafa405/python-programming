# Text to Handwriting using Python.
import pywhatkit as pw
txt= """ I am Hammad Mustafa.
I am 19 Years Old.
I want to become an Ai Expert and a Businessman."""

pw.text_to_handwriting(txt,"hammad.png",(0,0,138))
print("End")