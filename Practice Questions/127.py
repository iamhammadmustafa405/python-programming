# 127: 2. Student Record System (Encapsulation + Validation)
# Create a class Student:

# Requirements:

# Private attributes: __name, __marks
# Use @property for both attributes
# Setter rules:
# Name cannot be empty
# Marks must be between 0 and 100
# Method:
# display() → prints student details

# Tasks:

# Ensure invalid data is rejected in setters
# Protect attributes using encapsulation


class Student:
    def __init__(self,name,marks):
        self.name = name  # Getting through the setter
        self.marks = marks  # # Getting through the setter
    

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if name == "":
            raise ValueError("Invalid Name!")
        self.__name= name
    
    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,marks):
        if marks< 0 or marks>100:
            raise ValueError("Invalid Marks!")
        self.__marks= marks
    
    def show(self):
        print(f"The Student Name is: {self.name}")
        print(f"The Student Marks are: {self.marks}")


# Checking Output
s1= Student("Hammad",56)
s1.name = "Huzaifa"
print(s1.name)
s1.show()



# Improved Code by Claude Sonnet 4.6


class Student:
    def __init__(self, name, marks):
        self.name = name      # uses setter → validation runs
        self.marks = marks    # uses setter → validation runs

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        if not name.strip().isalpha():
            raise ValueError("Name must contain only letters.")
        self.__name = name.strip()

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        if not isinstance(marks, (int, float)):
            raise TypeError("Marks must be a number.")
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100.")
        self.__marks = marks

    def display(self):                       # renamed from show() to match spec
        print(f"Student Name:  {self.name}")
        print(f"Student Marks: {self.marks}")


# Testing valid data
s1 = Student("Hammad", 56)
s1.name = "Huzaifa"
print(s1.name)
s1.display()

# Testing invalid data — these should raise errors
try:
    s1.marks = 150
except ValueError as e:
    print(e)   # Marks must be between 0 and 100.

try:
    s1.name = ""
except ValueError as e:
    print(e)   # Name cannot be empty.