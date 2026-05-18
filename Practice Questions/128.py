# 128: 3. Shape Area System (Abstraction)
# Create an abstract class Shape:

# Requirements:

# Use ABC module
# Abstract method: area()

# Create two child classes:

# Rectangle (length, width)
# Circle (radius)

# Tasks:

# Each class must implement area() method
# Do not allow direct object creation of Shape
# Demonstrate abstraction by calling area() on different shapes

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length= length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        print(f"The area of the rectangle is: {self.area()}")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius *self.radius
    
    def display(self):
        print(f"The area of the circle is: {self.area()}")

r1= Rectangle(5,6)
r1.display()
c1= Circle(5)
c1.display()