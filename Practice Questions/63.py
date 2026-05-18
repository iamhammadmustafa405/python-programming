# 63: Remove duplicates from a list (using loop logic).
list= [4,5,2,4,7,9,4,3]
list_2= []
for i in list:
    if i not in list_2:
        list_2.append(i)
print(f"The List without duplicates is: {list_2}")