# 118: Create a class Book with attributes title and author. Create two objects and display their data.
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def show(self):
        print(f"The Title of the Book is {self.title} and Author is: {self.author}")
    
b1= Book("Islam", "Dr.Tahir-ul-Qadri")
b2= Book("Python", "Hammad Mustafa")
b1.show()
b2.show()