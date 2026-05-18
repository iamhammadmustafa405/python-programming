# 144: 3. List Index Access (Custom Error + Multiple except)
# Write a program that:

# Creates a list of 5 numbers
# Asks the user to enter an index to access

# Requirements:

# Handle:
# IndexError → if index is out of range
# ValueError → if input is not an integer
# If index is negative, manually raise an error using raise ValueError("Negative index not allowed")
# Use else to print the selected element
# Use finally to print: "Index access attempt done"
try:
    lst= [2,4,6,8,7]
    idx= int(input("Enter the index: "))
    if idx < 0:
        raise ValueError("Negative index is not allowed!")
    value = lst[idx]

except ValueError as e:
    print(f"Invalid Input: {e} ")

except IndexError:
    print("Index is out of range!")

else:
    print(f"Selected Element: {value}")

finally:
    print("Index access attempt done!")