# 61: Count how many times a specific element appears in a list.
list= [5,6,3,5,89,3,5,7,2]
n= int(input("Enter the Number You Want to check its Occurrances in the list: "))
count= 0
for i in list:
    if i == n:
        count+=1
print(f"{count} times {n} Repeats in the list.")