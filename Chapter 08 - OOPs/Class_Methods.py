# Different Methods to change the class Attribute


# 1. Directly using the Class Name (most common)
# class Student:
#     school_name = "ABC School"

# Student.school_name = "XYZ School"

# This updates the class attribute for all instances.

# 2. Using an Object (instance)
# s1 = Student()
# s1.school_name = "New School"

# Important:
# This does not change the class attribute. It creates a new instance variable for s1.

# To actually change the class attribute via object:

# s1.__class__.school_name = "XYZ School"
# 3. Inside the Class (using instance method)
# class Student:
#     school_name = "ABC School"

#     def change_school(self, new_name):
#         Student.school_name = new_name
# 4. Using setattr()
# setattr(Student, "school_name", "XYZ School")

# This dynamically changes the class attribute.

# 5. Using Class Reference (cls) indirectly

# Even without @classmethod, you can still access the class:

# class Student:
#     school_name = "ABC School"

#     def change_school(self, new_name):
#         self.__class__.school_name = new_name
# Key Insight
# Best practice: Use class name or class methods
# Avoid confusion: Changing via instance can create separate variables instead of updating the class


class Person:
    name= "Hammad Mustafa"

    def change_name(self,name):
        self.__class__.name= name  # Method 1

# p= Person()
# print(p.name)
# p.change_name("Huzaifa Mustafa")
# print(p.name)
# print(Person.name) 

class Person:
    name= "Hammad Mustafa"

    def change_name(self,name):
        Person.name = name   # Method 2
# p= Person()
# print(p.name)
# p.change_name("Huzaifa Mustafa")
# print(p.name)
# print(Person.name) 


# By Using Class Method
class Person:
    name= "Hammad Mustafa"
    @classmethod
    def change_name(cls,name):
        cls.name = name   # Method 3