# Question - 11: Write a program to find the greatest of 3 numbers entered by the user.
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))

if num1>=num2 and num1>=num3:
    print(f"{num1} is largest.")
elif(num2>=num3):
    print(f"{num2} is largest.")
else:
    print(f"{num3} is largest.")
# 2nd Method.
# print(f"You entered: {num1},{num2},{num3}")
# print(f"The greatest number is: {max(num1,num2,num3)}")