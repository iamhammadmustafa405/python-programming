# 59: Find the largest number in a list.
list= [4,5,89,45,234,4,67]
max= list[0]
for i in list:
    if i > max:
        max= i
print(f"{max} is the largest Number in the list.")