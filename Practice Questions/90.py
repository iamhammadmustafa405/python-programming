# 90: Write a function to print the length of the list
list1 = []
for i in range(5):
    n= int(input("Enter a Number: "))  # This code is for taking  input form the user.
    list1.append(n)


def length(list):
    print(len(list))


length(list1)