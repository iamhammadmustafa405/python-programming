# 131: Multi-level Inheritance with super()
# Create three classes:
# Animal → method sound()
# Dog (inherits from Animal) → overrides sound()
# Puppy (inherits from Dog) → overrides sound()

# Tasks:

# Each class should print its own message
# Use super() in each overridden method to call the parent version
# Show how method calls flow from Puppy → Dog → Animal

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Barks")
class Puppy(Dog):
    def sound(self):
        super().sound()
        print("bow!")

animal= Animal()
animal.sound()
dog= Dog()
dog.sound()
puppy = Puppy()
puppy.sound()