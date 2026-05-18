# Question - 04: Take two numbers and print whether their sum is even or odd.
num1= int(input("Enter a Number: "))
num2= int(input("Enter a Number: "))
sum= num1 + num2
print("The sum is even.") if sum % 2 == 0 else print("The sum is odd.")