# 34: Find the smallest digit in a given number.
n= int(input("Enter a Number: "))
min= n%10
while n>0:
    digit= n%10
    if digit < min:
        min= digit
    n= n//10
print(f"The Smallest digit in the Number is: {min}")