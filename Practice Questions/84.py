# 84: Write a function to calculate the factorial of a number.
def fact(n):
    fact= 1
    for i in range(1,n+1):
        fact *=i
    print(f"The Factorial of {n} is {fact}")

fact(7)