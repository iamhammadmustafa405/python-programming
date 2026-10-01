# # OOP in Python — Full Beginner Guide

# **OOP = Object-Oriented Programming.**

# It is a way of writing programs by organizing code around **objects**.

# For example, a student can be an object:

# ```text
# Student
# ├── name
# ├── age
# ├── marks
# └── study()
# ```

# Here:

# * `name`, `age`, `marks` → **attributes/data**
# * `study()` → **method/behavior**

# Python's OOP system is built around **classes and objects**.

# ---

# # 1. Class

# A **class** is like a blueprint/template.

# ```python
# class Student:
#     pass
# ```

# This creates a class called `Student`.

# Think:

# ```text
# Class = Blueprint
# Object = Actual thing made from blueprint
# ```

# ---

# # 2. Object

# An object is an actual instance of a class.

# ```python
# class Student:
#     pass

# student1 = Student()
# ```

# Here:

# ```text
# Student → class
# student1 → object
# ```

# You can create multiple objects:

# ```python
# student1 = Student()
# student2 = Student()
# student3 = Student()
# ```

# All are objects of the `Student` class.

# ---

# # 3. Attributes

# Attributes are **data belonging to an object**.

# ```python
# class Student:
#     pass

# student1 = Student()

# student1.name = "Hammad"
# student1.age = 19
# ```

# Now:

# ```python
# print(student1.name)
# print(student1.age)
# ```

# Output:

# ```text
# Hammad
# 19
# ```

# ---

# # 4. `__init__()` Constructor

# Instead of manually assigning attributes:

# ```python
# student1.name = "Hammad"
# student1.age = 19
# ```

# we can use `__init__()`.

# ```python
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# ```

# Now:

# ```python
# student1 = Student("Hammad", 19)
# ```

# Python automatically calls:

# ```python
# __init__()
# ```

# So:

# ```python
# print(student1.name)
# print(student1.age)
# ```

# Output:

# ```text
# Hammad
# 19
# ```

# ### Important

# `__init__()` is commonly called the **constructor**, although technically Python's object creation process involves `__new__()` first and `__init__()` initializes the object.

# For beginner OOP, remember:

# > `__init__()` initializes the object's data.

# ---

# # 5. `self`

# `self` refers to the **current object**.

# Example:

# ```python
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# ```

# When:

# ```python
# student1 = Student("Hammad", 19)
# ```

# Think:

# ```text
# self → student1
# ```

# So:

# ```python
# self.name
# ```

# means:

# ```text
# student1.name
# ```

# If:

# ```python
# student2 = Student("Ali", 20)
# ```

# then inside that call:

# ```text
# self → student2
# ```

# ---

# # 6. Methods

# A function inside a class is called a **method**.

# ```python
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print("My name is", self.name)
# ```

# Now:

# ```python
# student1 = Student("Hammad")

# student1.introduce()
# ```

# Output:

# ```text
# My name is Hammad
# ```

# ---

# # 7. Multiple Objects

# ```python
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(self.name, self.age)
# ```

# Create two objects:

# ```python
# student1 = Student("Hammad", 19)
# student2 = Student("Ali", 20)

# student1.introduce()
# student2.introduce()
# ```

# Output:

# ```text
# Hammad 19
# Ali 20
# ```

# Each object has its **own data**.

# ---

# # 8. Instance Attributes

# Attributes belonging to a particular object are called **instance attributes**.

# ```python
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# ```

# Here:

# ```text
# self.name
# self.age
# ```

# are instance attributes.

# For example:

# ```text
# student1.name → Hammad
# student2.name → Ali
# ```

# ---

# # 9. Class Attributes

# A **class attribute** belongs to the class and is shared by objects unless an instance overrides it.

# ```python
# class Student:

#     university = "NUST"

#     def __init__(self, name):
#         self.name = name
# ```

# Now:

# ```python
# student1 = Student("Hammad")
# student2 = Student("Ali")

# print(student1.university)
# print(student2.university)
# ```

# Both get:

# ```text
# NUST
# ```

# The class has one shared `university` attribute.

# ---

# # 10. Instance vs Class Attributes

# ```python
# class Student:

#     university = "NUST"       # class attribute

#     def __init__(self, name):
#         self.name = name      # instance attribute
# ```

# | Attribute    | Belongs to        |
# | ------------ | ----------------- |
# | `self.name`  | Individual object |
# | `university` | Class             |

# Think:

# ```text
# Student class
#     │
#     ├── university = "NUST"
#     │
#     ├── student1 → name = "Hammad"
#     │
#     └── student2 → name = "Ali"
# ```

# ---

# # 11. Instance Methods

# The most common method type.

# ```python
# class Student:

#     def introduce(self):
#         print("I am a student")
# ```

# It receives `self`.

# ```python
# student1.introduce()
# ```

# ---

# # 12. Class Methods

# A class method works with the **class**, rather than a particular instance.

# Use:

# ```python
# @classmethod
# ```

# and usually `cls`.

# ```python
# class Student:

#     university = "NUST"

#     @classmethod
#     def change_university(cls, name):
#         cls.university = name
# ```

# Call:

# ```python
# Student.change_university("FAST")
# ```

# Now:

# ```python
# print(Student.university)
# ```

# Output:

# ```text
# FAST
# ```

# ### `self` vs `cls`

# ```text
# self → current object
# cls  → current class
# ```

# ---

# # 13. Static Methods

# A static method doesn't automatically receive `self` or `cls`.

# Use:

# ```python
# @staticmethod
# ```

# Example:

# ```python
# class Math:

#     @staticmethod
#     def add(a, b):
#         return a + b
# ```

# Call:

# ```python
# print(Math.add(10, 20))
# ```

# Output:

# ```text
# 30
# ```

# It is placed inside the class because it is logically related to the class, but it doesn't need object/class data.

# ---

# # 14. Three Types of Methods

# | Method          | Decorator       | First parameter |
# | --------------- | --------------- | --------------- |
# | Instance method | None            | `self`          |
# | Class method    | `@classmethod`  | `cls`           |
# | Static method   | `@staticmethod` | None            |

# ---

# # 15. Encapsulation

# **Encapsulation** means keeping data and the methods that work with that data together inside a class, while controlling how the data is accessed.

# Python doesn't enforce private fields in exactly the same way as languages such as Java or C++.

# Python commonly uses naming conventions.

# ### Public

# ```python
# self.name
# ```

# Accessible normally.

# ### "Protected" convention

# ```python
# self._name
# ```

# The single underscore means:

# > "This is intended for internal/subclass use."

# It is a convention, not strict privacy.

# ### Name-mangled

# ```python
# self.__salary
# ```

# Double underscore triggers **name mangling**.

# Example:

# ```python
# class Employee:

#     def __init__(self):
#         self.__salary = 50000
# ```

# This isn't normally accessed as:

# ```python
# employee.__salary
# ```

# Python internally changes the name roughly to:

# ```text
# _Employee__salary
# ```

# This is **name mangling**, not absolute private access.

# ---

# # 16. Getters and Setters

# Suppose we want controlled access to data.

# ```python
# class Student:

#     def __init__(self, age):
#         self.__age = age

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
# ```

# Usage:

# ```python
# student = Student(19)

# print(student.get_age())

# student.set_age(20)
# ```

# ---

# # 17. `@property`

# Python provides a cleaner way to create managed attributes.

# ```python
# class Student:

#     def __init__(self, age):
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, value):
#         if value >= 0:
#             self.__age = value
# ```

# Now:

# ```python
# student = Student(19)

# print(student.age)

# student.age = 20
# ```

# It looks like a normal attribute, but Python is actually calling the property methods.

# ---

# # 18. Inheritance

# **Inheritance** allows one class to reuse/extend another class.

# Parent class:

# ```python
# class Animal:

#     def eat(self):
#         print("Eating")
# ```

# Child class:

# ```python
# class Dog(Animal):
#     pass
# ```

# Now:

# ```python
# dog = Dog()

# dog.eat()
# ```

# Output:

# ```text
# Eating
# ```

# `Dog` inherited `eat()` from `Animal`.

# ---

# # 19. Parent and Child

# Terminology:

# ```text
# Animal → Parent / Base / Superclass

# Dog → Child / Derived / Subclass
# ```

# ---

# # 20. Adding New Methods to Child

# ```python
# class Animal:

#     def eat(self):
#         print("Eating")


# class Dog(Animal):

#     def bark(self):
#         print("Woof!")
# ```

# Now:

# ```python
# dog = Dog()

# dog.eat()
# dog.bark()
# ```

# Output:

# ```text
# Eating
# Woof!
# ```

# The child gets the parent's functionality and can add its own.

# ---

# # 21. Method Overriding

# A child can replace a method inherited from its parent.

# ```python
# class Animal:

#     def sound(self):
#         print("Some sound")


# class Dog(Animal):

#     def sound(self):
#         print("Woof!")
# ```

# Now:

# ```python
# dog = Dog()

# dog.sound()
# ```

# Output:

# ```text
# Woof!
# ```

# The child method **overrides** the parent method.

# ---

# # 22. `super()`

# `super()` allows a child class to access the parent implementation.

# ```python
# class Animal:

#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):

#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
# ```

# Now:

# ```python
# dog = Dog("Max", "German Shepherd")

# print(dog.name)
# print(dog.breed)
# ```

# Output:

# ```text
# Max
# German Shepherd
# ```

# Without `super()`, you'd have to initialize the parent part yourself.

# ---

# # 23. Multilevel Inheritance

# Inheritance can happen in multiple levels.

# ```text
# Animal
#    ↓
# Mammal
#    ↓
# Dog
# ```

# Python:

# ```python
# class Animal:
#     def eat(self):
#         print("Eating")


# class Mammal(Animal):
#     def walk(self):
#         print("Walking")


# class Dog(Mammal):
#     def bark(self):
#         print("Barking")
# ```

# Now `Dog` can access:

# ```python
# dog = Dog()

# dog.eat()
# dog.walk()
# dog.bark()
# ```

# ---

# # 24. Multiple Inheritance

# A class can inherit from multiple classes.

# ```python
# class Father:

#     def skills(self):
#         print("Driving")


# class Mother:

#     def hobby(self):
#         print("Painting")


# class Child(Father, Mother):
#     pass
# ```

# Now:

# ```python
# child = Child()

# child.skills()
# child.hobby()
# ```

# The child gets functionality from both parents.

# ---

# # 25. Hierarchical Inheritance

# One parent can have multiple children.

# ```text
#        Animal
#        /    \
#      Dog    Cat
# ```

# Python:

# ```python
# class Animal:
#     def eat(self):
#         print("Eating")


# class Dog(Animal):
#     def bark(self):
#         print("Woof")


# class Cat(Animal):
#     def meow(self):
#         print("Meow")
# ```

# Both `Dog` and `Cat` inherit from `Animal`.

# ---

# # 26. Hybrid Inheritance

# A combination of different inheritance patterns.

# For example:

# ```text
#        A
#       / \
#      B   C
#       \ /
#        D
# ```

# Python supports such structures, but complex inheritance should be designed carefully.

# ---

# # 27. Polymorphism

# **Poly = many**

# **Morphism = forms**

# So polymorphism means that the **same interface/method name can behave differently for different objects**.

# Example:

# ```python
# class Dog:

#     def sound(self):
#         print("Woof")


# class Cat:

#     def sound(self):
#         print("Meow")
# ```

# Now:

# ```python
# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()
# ```

# Output:

# ```text
# Woof
# Meow
# ```

# Same method name:

# ```text
# sound()
# ```

# Different behavior.

# ---

# # 28. Duck Typing

# Python strongly uses **duck typing**.

# The idea is:

# > If an object behaves like the required object, Python often doesn't care about its exact class.

# Example:

# ```python
# class Dog:

#     def sound(self):
#         print("Woof")


# class Cat:

#     def sound(self):
#         print("Meow")


# def make_sound(animal):
#     animal.sound()
# ```

# Now:

# ```python
# make_sound(Dog())
# make_sound(Cat())
# ```

# Output:

# ```text
# Woof
# Meow
# ```

# `make_sound()` doesn't need to check whether it received a `Dog` or `Cat`.

# It only needs the object to have:

# ```python
# sound()
# ```

# ---

# # 29. Abstraction

# **Abstraction** means exposing the important interface while hiding implementation details.

# Python provides the `abc` module for formal abstract base classes.

# ```python
# from abc import ABC, abstractmethod
# ```

# Example:

# ```python
# from abc import ABC, abstractmethod


# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass
# ```

# Now a child class must implement `sound()`:

# ```python
# class Dog(Animal):

#     def sound(self):
#         print("Woof")
# ```

# You generally cannot instantiate the abstract class:

# ```python
# animal = Animal()
# ```

# This raises an error because `Animal` has an abstract method.

# ---

# # 30. Abstract Class

# An abstract class is generally used as a **template/interface** for subclasses.

# ```python
# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass
# ```

# Child:

# ```python
# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
# ```

# Now:

# ```python
# circle = Circle(5)

# print(circle.area())
# ```

# ---

# # 31. The Four Main OOP Principles

# The classic four pillars are:

# ```text
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction
# ```

# ### Easy memory trick

# ```text
# E → Encapsulation → control/organize data
# I → Inheritance   → reuse
# P → Polymorphism  → many forms
# A → Abstraction   → hide implementation details
# ```

# ---

# # 32. Special / Magic / Dunder Methods

# Methods surrounded by double underscores are commonly called **dunder methods**.

# Example:

# ```python
# __init__
# ```

# Other examples:

# ```text
# __str__
# __repr__
# __len__
# __eq__
# __lt__
# __add__
# __sub__
# __mul__
# ```

# They allow your objects to work naturally with Python's operators and built-in functions.

# ---

# # 33. `__str__()`

# Controls what happens when you use `str()` or usually `print()` on an object.

# Without `__str__()`:

# ```python
# class Student:

#     def __init__(self, name):
#         self.name = name
# ```

# Printing the object gives a default representation that isn't very user-friendly.

# With:

# ```python
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Student: {self.name}"
# ```

# Now:

# ```python
# student = Student("Hammad")

# print(student)
# ```

# Output:

# ```text
# Student: Hammad
# ```

# ---

# # 34. `__repr__()`

# `__repr__()` is intended to provide a useful developer-oriented representation of an object.

# ```python
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Student({self.name!r})"
# ```

# Then:

# ```python
# student = Student("Hammad")

# print(repr(student))
# ```

# Output:

# ```text
# Student('Hammad')
# ```

# A good `repr` is often useful for debugging.

# ---

# # 35. Operator Overloading

# Python allows classes to define how operators work with their objects.

# For example:

# ```python
# a + b
# ```

# normally means addition.

# But you can define what `+` means for your class using:

# ```python
# __add__()
# ```

# Example:

# ```python
# class Number:

#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return Number(self.value + other.value)
# ```

# Now:

# ```python
# a = Number(10)
# b = Number(20)

# c = a + b

# print(c.value)
# ```

# Output:

# ```text
# 30
# ```

# ---

# # 36. Common Operator Dunder Methods

# | Operator | Method           |
# | -------- | ---------------- |
# | `+`      | `__add__()`      |
# | `-`      | `__sub__()`      |
# | `*`      | `__mul__()`      |
# | `/`      | `__truediv__()`  |
# | `//`     | `__floordiv__()` |
# | `%`      | `__mod__()`      |
# | `**`     | `__pow__()`      |
# | `==`     | `__eq__()`       |
# | `<`      | `__lt__()`       |
# | `>`      | `__gt__()`       |
# | `<=`     | `__le__()`       |
# | `>=`     | `__ge__()`       |
# | `!=`     | `__ne__()`       |
# | `len(x)` | `__len__()`      |

# ---

# # 37. `__len__()`

# Allows your object to work with `len()`.

# ```python
# class Team:

#     def __init__(self, players):
#         self.players = players

#     def __len__(self):
#         return len(self.players)
# ```

# Now:

# ```python
# team = Team(["Ali", "Hammad", "Ahmed"])

# print(len(team))
# ```

# Output:

# ```text
# 3
# ```

# ---

# # 38. `isinstance()`

# Checks whether an object belongs to a class.

# ```python
# class Student:
#     pass

# student = Student()

# print(isinstance(student, Student))
# ```

# Output:

# ```text
# True
# ```

# With inheritance:

# ```python
# class Animal:
#     pass

# class Dog(Animal):
#     pass

# dog = Dog()

# print(isinstance(dog, Dog))
# print(isinstance(dog, Animal))
# ```

# Both are:

# ```text
# True
# ```

# because a `Dog` is also an `Animal`.

# ---

# # 39. `issubclass()`

# Checks whether one class is a subclass of another.

# ```python
# class Animal:
#     pass

# class Dog(Animal):
#     pass

# print(issubclass(Dog, Animal))
# ```

# Output:

# ```text
# True
# ```

# ---

# # 40. Composition

# Composition means one object **contains another object**.

# Instead of inheritance:

# ```text
# Car IS-A Vehicle
# ```

# Composition:

# ```text
# Car HAS-A Engine
# ```

# Example:

# ```python
# class Engine:

#     def start(self):
#         print("Engine started")


# class Car:

#     def __init__(self):
#         self.engine = Engine()

#     def start(self):
#         self.engine.start()
# ```

# Now:

# ```python
# car = Car()

# car.start()
# ```

# Output:

# ```text
# Engine started
# ```

# The `Car` **has an** `Engine`.

# ---

# # 41. Inheritance vs Composition

# ### Inheritance

# ```text
# Dog IS-A Animal
# ```

# ```python
# class Dog(Animal):
#     pass
# ```

# ### Composition

# ```text
# Car HAS-A Engine
# ```

# ```python
# class Car:
#     def __init__(self):
#         self.engine = Engine()
# ```

# A useful rule:

# > **IS-A → often inheritance**
# > **HAS-A → often composition**

# ---

# # 42. Class Relationships

# You will commonly see:

# ```text
# Inheritance
#     IS-A

# Composition
#     HAS-A

# Aggregation
#     HAS-A / uses another object, often with more independent lifetimes
# ```

# For beginner OOP, focus first on inheritance and composition.

# ---

# # 43. Object Identity

# Every object has an identity.

# ```python
# class Student:
#     pass

# a = Student()
# b = Student()
# ```

# Even though both belong to the same class:

# ```python
# print(a is b)
# ```

# Output:

# ```text
# False
# ```

# They are two different objects.

# ---

# # 44. `is` vs `==`

# `==` checks **equality**.

# `is` checks **identity**.

# ```python
# a = [1, 2]
# b = [1, 2]

# print(a == b)
# print(a is b)
# ```

# Output:

# ```text
# True
# False
# ```

# Why?

# ```text
# a and b
# → same contents
# → different objects
# ```

# ---

# # 45. Complete OOP Example

# Here is a small example combining several concepts:

# ```python
# class Student:

#     university = "NUST"

#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def introduce(self):
#         print(f"My name is {self.name}.")
#         print(f"I am {self.age} years old.")

#     def is_passed(self):
#         return self.marks >= 50

#     def __str__(self):
#         return f"{self.name} - {self.marks}"


# student = Student("Hammad", 19, 85)

# student.introduce()

# print(student.is_passed())
# print(student)
# ```

# Output:

# ```text
# My name is Hammad.
# I am 19 years old.
# True
# Hammad - 85
# ```

# This example contains:

# ```text
# class
# object
# __init__
# self
# instance attributes
# class attribute
# methods
# return
# __str__
# ```

# ---

# # 46. OOP Structure to Memorize

# ```text
#                     OOP
#                      │
#        ┌─────────────┴─────────────┐
#        │                           │
#      Class                       Object
#        │                           │
#    ┌───┴────┐                Attributes
#    │        │                Methods
# Attributes Methods
# ```

# Then:

# ```text
# OOP
# │
# ├── Classes & Objects
# ├── __init__()
# ├── self
# ├── Instance Attributes
# ├── Class Attributes
# ├── Methods
# │   ├── Instance
# │   ├── Class
# │   └── Static
# │
# ├── Encapsulation
# │   ├── Public
# │   ├── _protected convention
# │   └── __name mangling
# │
# ├── Inheritance
# │   ├── Single
# │   ├── Multilevel
# │   ├── Multiple
# │   ├── Hierarchical
# │   └── Hybrid
# │
# ├── Polymorphism
# │   ├── Overriding
# │   └── Duck typing
# │
# ├── Abstraction
# │   └── ABC / abstractmethod
# │
# ├── Magic / Dunder Methods
# │   ├── __init__
# │   ├── __str__
# │   ├── __repr__
# │   ├── __len__
# │   └── operator methods
# │
# ├── Composition
# ├── Properties
# ├── super()
# └── isinstance() / issubclass()
# ```

# ## Most important topics to learn first

# If you're learning OOP from beginner level, learn them in this order:

# **1. Class → 2. Object → 3. `__init__()` → 4. `self` → 5. Attributes → 6. Methods → 7. Class vs instance attributes → 8. Inheritance → 9. `super()` → 10. Method overriding → 11. Polymorphism → 12. Encapsulation → 13. `@property` → 14. Class/static methods → 15. Abstraction → 16. Dunder methods → 17. Composition.**
