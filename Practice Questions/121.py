# 121: Create a class Circle with radius. Add a method to calculate circumference.
class Circle: 
    def __init__(self,radius):
        self.radius = radius
    
    def circumference(self):
        return 2* 3.14 * self.radius
    
c1= Circle(5)
print(f"The Circumference of the Circle is: {c1.circumference()}")