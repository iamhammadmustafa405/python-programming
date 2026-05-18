# 130: Method Overriding with super()
# Create a base class Vehicle with a method start() that prints "Vehicle is starting".
# Create a child class Car that overrides start().

# Tasks:

# In the overridden method, first call the parent method using super()
# Then print "Car is ready to drive"
# Create objects and demonstrate both behaviors

class Vehicle:
    
    def start(self):
        print("Vehicle is Starting...")

class Car(Vehicle):

    def start(self):
        super().start()
        print("Car is ready to drive.")
v= Vehicle()
v.start()
c= Car()
c.start()