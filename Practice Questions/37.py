# 37: Calculate the product of digits of a number (e.g., 123 → 1×2×3).
n= int(input("Enter a Number: "))
product=1
while n>0:
    digit = n%10
    product *=digit
    n= n//10
print(f"The Product of digits of the Number is: {product}")