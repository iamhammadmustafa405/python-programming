# 33: Find the largest digit in a given number using a while loop.
n= int(input("Enter a Number: "))
max= n%10
while n>0:
    digit = n%10
    if digit > max:
        max = digit
    n= n//10
print(f"The Maximum digit in the number is: {max}")