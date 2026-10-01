# Getter and Setter MEthod in Python


# Old MEthod:

# class Person:
#     def __init__(self,name):
#         self.__name = name

    
#     def get_name(self):   # -----> Getter
#         return self.__name
    
#     def set_name(self,name):  # -----> Setter
#         self.__name = name


# p1= Person("Hammad")
# print(p1.get_name())
# p1.set_name("Huzaifa")
# print(p1.get_name())





# ------------>                     Notes:-

# Getter and setter methods are used in object-oriented programming to safely access and update the values of private attributes in a class.
# Simple idea


# Getter method → used to get (read) the value of a private variable


# Setter method → used to set (update/change) the value of a private variable



# Why we need them?
# If we make variables private (hidden), we cannot access them directly from outside the class. So we use getters and setters to control how they are used.

# Easy Python example
# class Person:    def __init__(self, name, age):  
#       self.__name = name   # private variable      
#   self.__age = age     # private variable   
#  # Getter method    \
# def get_name(self):        
# return self.__name   
#  # Setter method    
# def set_name(self, name):       
#  self.__name = name

# How it works
# p = Person("Ali", 20)
# print(p.get_name())   # Getter → gives name
# p.set_name("Ahmed")   
# # Setter → changes name
# print(p.get_name())   # Now updated name
# __________________________________________________________________________________________________________________________________________

#                                                New Method (Pythonic Way)

# Using @ property Decorator:

# In Python, @property is a modern and cleaner way to create getter and setter methods without calling them like normal functions.

# It allows you to access methods like variables.

# 1. Basic idea

# Instead of writing:

# obj.get_name()
# obj.set_name("Ali")

# You can write:

# obj.name
# obj.name = "Ali"

# But still keep control inside the class.

# 2. Example using @property
# class Person:
#     def __init__(self, name):
#         self.__name = name   # private variable

#     # Getter
#     @property
#     def name(self):
#         return self.__name

# Now you can use it like this:
# p = Person("Ali")

# print(p.name)   # calls getter automatically

# 3. Adding Setter with @property

# If you want to also allow updating the value:

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     # Getter
#     @property
#     def name(self):
#         return self.__name

#     # Setter
#     @name.setter
#     def name(self, value):
#         self.__name = value
# Now usage becomes:
# p = Person("Ali")

# print(p.name)     # getter runs

# p.name = "Ahmed"  # setter runs

# print(p.name)
# 4. Why @property is better

# Looks like normal variable access
# Cleaner and more readable
# Still controls access (encapsulation)
# No need for get_ and set_ function names
# 5. Simple summary
# @property → makes a method behave like a variable (getter)
# @name.setter → allows controlled updating of that variable




# Code:- 

class Person: 
    def __init__(self,name):
        self.__name = name

    # getter
    @property
    def name(self):
        return self.__name
    
    # setter
    @name.setter
    def name(self,name):
        self.__name = name

p1= Person("Hammad")
print(p1.name)  #  Calling Getter
p1.name = "Huzaifa" # Calling Setter
print(p1.name) 