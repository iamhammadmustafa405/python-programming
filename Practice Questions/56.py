# 56: ind the factorial of a number using for loop.
n= int(input("Enter a Number: "))
fact= 1
for i in range (1,n+1):
    fact*=i
print(f"The Factorial of the given Number is: {fact}")