# 126: Bank Account (Encapsulation + Getter/Setter)
# Create a class BankAccount:

# Requirements:

# Private attribute: __balance
# Constructor to initialize balance
# Getter method using @property → balance
# Setter method to update balance (only if value is positive)
# Methods:
# deposit(amount) → adds money
# withdraw(amount) → subtracts money if enough balance exists

# Tasks:

# Prevent direct access to __balance
# Ensure negative balance is not allowed
# Use @property and @balance.setter

class Bank_Account:
    def __init__(self,balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,balance):
        if balance <=0:
            print("Invalid Balance Update")
            return
        self.__balance = balance
    
    
    def deposit(self,amt):
        print(f"Your Current Balance is: {self.balance}")
        if amt <=0:
            print("Invalid Amount!")
            return
        self.__balance += amt
        print(f"Deposited:  {amt}")
        print(f"Your updated Balance is: {self.balance}")


    def withdraw(self,amt):
        print(f"Your Current Balance is: {self.balance}")
        if amt <=0:
            print("Invalid Amount!")
            return
        elif amt > self.__balance:
            print ("You Don't have Enough Money!")
            return
        self.__balance -= amt
        print(f"Withdrawal:  {amt}")
        print(f"Your updated Balance is: {self.balance}")

a1= Bank_Account(4500)
print(a1.balance) # Getter
a1.balance = 7000  # Setter
print(a1.balance) 
a1.deposit(6000) # Deposit
a1.withdraw(3000) # Withdrawal

a1.balance = -600  # Checking Setter 
print(a1.balance)