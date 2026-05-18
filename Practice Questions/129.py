# 129: Basic Inheritance with super() (Constructor Use)
# Create a parent class Person with attributes name and age.
# Create a child class Student that adds student_id.

# Tasks:

# Use super() to call the parent constructor
# Add a method display_info() in both classes
# Override the method in Student and include parent data using super()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Your name is {self.name} and Your age is {self.age}")
    
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age) # Super method() gives all attributes to child class we don't need to make again.
        self.student_id = student_id
    def display_info(self):
        super().display_info() # This method uses the all previous  version of data of parent class here
        print(f"Your student_id is {self.student_id}")

s1= Student("Hammad",19,4)
s1.display_info()