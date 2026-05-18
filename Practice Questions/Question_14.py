# Question - 14: Take 5 numbers from the user and store them in a list.
# num1= int(input("Enter a number:"))
# num2= int(input("Enter a number:"))
# num3= int(input("Enter a number:"))
# num4= int(input("Enter a number:"))
# num5= int(input("Enter a number:"))
# numbers = [num1,num2, num3, num4, num5]
# print(f"The list of your numbers is: {numbers}")

# 2nd Method.
numbers= []
for i in range(5):
    num= int(input("Enter a Number:"))
    numbers.append(num)
print(f"The list of numbers: {numbers}")