 # 132: Create a system for an Employee Management System using inheritance.
# Requirements
# 1. Parent Class: Employee
# Attributes:
# name
# salary
# Methods:
# display_info() → prints name and salary
# 2. Child Class: Manager (inherits Employee)
# Additional attribute:
# department
# Tasks:
# Use super() in constructor to set name and salary
# Add department in child class
# Override display_info()
# First call parent method using super()
# Then print department
# 3. Child Class: TeamLead (inherits Manager)
# Additional attribute:
# team_size
# Tasks:
# Use super() to call Manager constructor
# Override display_info()
# Call parent (Manager) method using super()
# Then print team size
# Extra Challenge (important)
# Create objects of:
# Employee
# Manager
# TeamLead
# Call display_info() on all of them
# Observe how super() builds layered behavior
# What this tests
# Multi-level inheritance
# Constructor chaining using super()
# Method overriding with parent reuse

class Employee:
    def __init__(self,name, salary):
        self.name= name
        self.salary = salary
    
    def display_info(self):
        print(f"Your name is {self.name} and your salary is {self.salary}.")
    
class Manager(Employee):
    def __init__(self,name, salary,department):
        super().__init__(name,salary)
        self.department =department

    def display_info(self):
        super().display_info()
        print(f"Your department is {self.department}")

class Teamlead(Manager):
    def __init__(self,name,salary,department,team_size):
        super().__init__(name,salary,department)
        self.team_size = team_size
    
    def display_info(self):
        super().display_info()
        print(f"The team size is {self.team_size}")

employee= Employee("Hammad",12000)
employee.display_info()
manager = Manager("Hammad",12000,"Nust")
manager.display_info()
teamlead= Teamlead("Hammad", 12000,"Nust",45)
teamlead.display_info()