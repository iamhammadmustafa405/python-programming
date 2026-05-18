# 140: Define a Employee Class with role, department and salary. This class also has a showdetails() method.
# --> Create an Engineer class that inherits properties from Employee and has additional attributes : name & age.
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department= department
        self.salary = salary
    
    def showdetails(self):
        return f"Your Role is: {self.role}, Your Department is: {self.department} and Your Salary is: {self.salary}."

class Engineer(Employee):
    def __init__(self,role,department,salary,name,age):
        super().__init__(role,department,salary)
        self.name = name
        self.age = age

    def showdetails(self):
        base= super().showdetails()
        return f"Your Name is: {self.name}, Your Age is: {self.age}, {base}"

employee= Employee("Scientist","SEECS", 45000)
print(employee.showdetails())
engineer = Engineer("Scientist", "SEECS", 45000, "Hammad Mustafa", 19)
print(engineer.showdetails())