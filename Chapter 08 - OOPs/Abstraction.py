# Abstraction: 
from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self): # Abstract method
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d= Dog()
d.sound()
c= Cat()
c.sound()