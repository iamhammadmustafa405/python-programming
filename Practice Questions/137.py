# 137:  Polymorphism (Same Method, Different Behavior)
# Create two classes:

# Cat → method sound() → returns "Meow"
# Dog → method sound() → returns "Bark"
class Cat:
    @staticmethod
    def sound():
        print("Meow")

class Dog:
    @staticmethod
    def sound():
        print("Bark")
c= Cat()
c.sound()
d= Dog()
d.sound()