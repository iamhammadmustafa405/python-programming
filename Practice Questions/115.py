# 115: Create a  Student class that takes name & Marks of 3 subjects as Argument in Constructors. Then Create a Method to print the average.
class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1= sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def avg(self):
        print(f"The Average of Marks is: {(self.sub1 +self.sub2 +self.sub3)/3}")

s1 = Student("Hammad",34,56,78)
s1.avg()