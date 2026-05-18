# 135: Create a class Student:
# Attributes: name, marks

# Implement __str__() to return:

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}"
    
s= Student("Hammad",100)
print(s)