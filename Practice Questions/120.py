# 120: Create a class Rectangle with length and width. Add a method to calculate area.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)
    
r1 = Rectangle(8, 4)
print(f"The Area of the Rectangle is : {r1.area()} m sq.")