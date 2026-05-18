# Question - 12: Write a program to find the greatest of 4 numbers entered by the user.
a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))
c= int(input("Enter 3rd number: "))
d= int(input("Enter 4th number: "))
# 1st Method:

# if a>=b and a>=c and a>=d:
#     print(f"{a} is the largest number.")
# elif b>=a and b>=c and b>=d:
#     print(f"{b} is the largest number.")
# elif c>=a and c>=b and c>=d:
#     print(f"{c} is the largest number.")
# else:
#     print(f"{d} is the largest number.")

# 2nd Method:
largest= a
if b> largest:
    largest= b
if c> largest:
    largest= c
if d>largest:
    largest = d
print(f"The largest number is: {largest}")