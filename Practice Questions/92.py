# 92: Write a function to find the factorial of n.
n= int(input("Enter a Number: "))

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(f"The factorial of {n} is {fact}.")

fact(n)