# 60: Find the smallest number in a list
list= []
for i in range(1,6):
    n= int(input("Enter a Number: "))    # -----> This is the part where i will take the input elements for the list from the user.
    list.append(n)
min= list[0]
for i in list:
    if i < min:
        min= i
print(f"{i} is the smallest number in the list.")