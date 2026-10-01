# # Classes  & Objects..
# class Student: # ------> Creating Class
#     name = "Hammad Mustafa"

# s1= Student()  # ------ Creating Object
# print(s1.name)

# s2= Student()
# print(s2.name)



# class Car:
#     color = "Red"
#     brand= "Mercedes"

# c1= Car()
# print(c1.color)
# print(c1.brand)


# Constructor:-
class Student:
    age = 19   # -----> # Class Attributes
    def __init__(self,name, marks):
        self.name= name
        self.marks = marks # -----> Instance/ Object Attributes
        print("Adding New Student to the Database.")

    def hello(self): # ----> class method
        print("Hey! I am Hammad Mustafa.")

    def show_marks(self): # ----> Instance Method
        return self.marks   
    

s1= Student("Hammad",78)
print(s1.name)
print(s1.age,s1.marks)
print(s1.show_marks())
# s2 = Student("Huzaifa",67)
# print(s2.name)
# print(s2.age,s2.marks)


# print(Student.age)


# Methods

# s1 = Student("Hammad", 56)
# s1.hello()
# print(s1.show_marks())


# Static Methods

# class Student:
#     @staticmethod # -----> static Method
#     def hello():
#         print("Hello")

# c1= Student()
# c1.hello()


# Abstraction
# class Car:
#     def __init__(self):
#         self.clutch = False
#         self.brk= False
#         self.acc= False
    
#     def start(self):
#         self.clutch= True  # Abstraction
#         self.acc = True
#         print("Car started...")

# car1= Car()
# car1.start()

# deleting object

# class Student:
#     def __init__(self,name):
#         self.name = name

# c1= Student("Hammad")
# del c1 ----> # It deletes the object....
# print(c1.name)





# # Private Attributes and Methods
# class Student:
#     __name = "Hammad"


#     def __hello(self):
#         print("Hello")

#     def welcome(self):
#         self.__hello()

# std1= Student()
# # print(std1.__name) # Gives Error
# # std1.__hello() # Gives Error
# # std1.welcome() # It Works because it use the private method inside it.

