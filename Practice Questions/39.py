# 39: Find the sum of digits of a number (e.g., 123 → 6).
n= int(input("Enter a Number: "))
sum= 0
while n>0:
    digit= n%10
    sum +=digit
    n= n//10
print(f"The Sum of digits is: {sum}")