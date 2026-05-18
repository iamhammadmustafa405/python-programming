# 139: Define a Circle class to create a circle with radius r using the constructor. 
# --> Define an area() method to calculate the area of the circle.
# --> define a circumference() method to calculate the circumference of the circle.

import math

class Circle:
    def __init__(self,r):
        self.r = r
    

    def area(self):
        return round(math.pi * self.r * self.r,2)


    def circumference(self):
        return round(2 * math.pi * self.r,2)    
    
    def display(self):
        print(f"The area of the circle is: {self.area()}")
        print(f"The circumference of the circle is: {self.circumference()}")

c= Circle(5)
c.display()