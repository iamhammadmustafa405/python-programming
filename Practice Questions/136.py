# 136: 3. Operator Overloading (+)
# Create a class BankAccount:

# Attribute: balance
# Implement __add__() so two accounts can be added

class BankAccount:
    def __init__(self,balance):
        if balance<0:
            raise ValueError("Invalid Balance!")
        self.balance = balance
    
    def __add__(self,acc2):
        if not isinstance(acc2,BankAccount):
            return NotImplemented
        return BankAccount(self.balance + acc2.balance)
    def __str__(self): 
        return f"Your Balance is: {self.balance}"
        
        
acc1= BankAccount(6000)
acc2 = BankAccount(4000)
total_balance= acc1 + acc2
print(total_balance)