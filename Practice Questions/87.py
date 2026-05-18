# 87: Write a Function to check if a number is positive, negative or zero.
n= int(input("Enter a Number: "))
def check(n):
    if n>0:
        print("The number is postive.")
    elif n<0:
        print("The number is negative.")
    else:
        print("The number is zero.")


check(n)