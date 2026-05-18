# 64: Create a new list with squares of numbers from another list.
num= [4,6,2,8,9,34]
sq= []
for i in num:
    square= i**2
    sq.append(square)
print(f"The list of Squares is: {sq}")