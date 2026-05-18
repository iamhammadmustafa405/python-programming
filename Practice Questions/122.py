# 122 : Create a class BankAccount with balance. Add methods deposit() and withdraw().
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    def deposit(self):
        print(f"Your Current Balance is: {self.balance}")
        amt= float(input("Enter the amount you want to deposit: "))
        self.balance += amt
        print(f"Your Current Balance is: {self.balance}")
    
    def withdraw(self):
        print(f"Your Current Balance is: {self.balance}")
        amt= float(input("Enter the amount you want to withdraw: "))
        self.balance -= amt
        print(f"Your Current Balance is: {self.balance}")

c1= BankAccount(50000)
c1.withdraw()