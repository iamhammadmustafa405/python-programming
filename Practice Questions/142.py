# 142: User Input Calculator (Multiple Exceptions + else + finally)
# Write a program that:

# Asks the user for two numbers and an operator (+, -, *, /)
# Performs the calculation

# Requirements:

# Handle:
# ValueError → if user enters non-numeric input
# ZeroDivisionError → if dividing by zero
# Invalid operator (use raise ValueError)
# Use else to print the result only if no error occurs
# Use finally to print: "Calculation attempt finished"

                                            # Bugged Code
# try: 
#     num1= int(input("Enter number 01: "))
#     num2= int(input("Enter number 02: "))
# except ValueError:
#     raise ValueError("Invalid Input!")

# opt= input("What do you want to do? ( +, -, *, /, %): ")

# if opt != "+" and opt != "-" and opt != "*" and opt != "/" and opt != "%":
#     raise ValueError("Invalid Operator!") 
# else:
#     if opt == "+":
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")
#     elif opt == "-":
#         result = num1 - num2
#         print(f"{num1} - {num2} = {result}")
#     elif opt == "*":
#         result = num1 * num2
#         print(f"{num1} x {num2} = {result}")
#     elif opt == "/":
#         result = num1 / num2
#         print(f"{num1} / {num2} = {result}")
#     elif opt == "%":
#         result = num1 % num2
#         print(f"{num1} % {num2} = {result}")

# print("Calculation Attempt Finished!")

#                                               Improved Code
try:
    num1 = int(input("Enter number 01: "))
    num2 = int(input("Enter number 02: "))
    opt = input("What do you want to do? ( +, - , *, /, %): ")

    if opt not in ["+", "-", "*", "/", "%"]:
        raise ValueError("Invalid Operator!")
    
    if opt == "+":
        result = num1 + num2 
    elif opt == "-":
        result = num1 - num2
    elif opt == "*":
        result = num1 * num2
    elif opt == "/":
        result = num1 /num2
    elif opt == "%":
        result = num1 % num2

except ValueError as e:
    print(f"Error: {e}")

except ZeroDivisionError:
    print("Divison by Zero is not Allowed!")

else:
    print(f"The Result is: {result}")

finally:
    print("Calculation Attempt Finished!")


# Key Concepts in Your Code
# try → run code that might fail
# raise → manually create an error
# except → handle errors
# else → run if everything is successful
# finally → always run