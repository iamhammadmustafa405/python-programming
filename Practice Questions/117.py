# 117: Create a class Student that stores name and age. Print student details.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1= Student("Hammad", 19)
print(s1.name, s1.age)