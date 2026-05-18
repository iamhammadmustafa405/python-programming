# 123: Create Account Class with 2 Attributes - balance & Account Number. Create methods for debit, credit and printing the balance.
class Account:
    
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    def withdraw(self,amt):
        print(f"Your Current Balance is: {self.balance}")
        if amt>self.balance:
            print("Insufficient Balance!")
            return
        elif amt<=0:
            print("Enter Valid Amount!")
            return
        self.balance -= amt
        print(f"Withdrawal: {amt}")
        self.show_balance()
    
    def deposit(self,amt):
        print(f"Your Current Balance is: {self.balance}")
        if amt<=0:
            print("Enter Valid Amount!")
            return
        self.balance += amt
        print(f"deposited: {amt}")
        self.show_balance()

    def show_balance(self):
        print(f"Your Updated Balance is : {self.balance}")

customer1= Account(4000,"pk56839242472")
customer1.deposit(5000)
