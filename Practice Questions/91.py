# 91: Write a Function to print the elements of the list in a single line.
list = []
for i in range(5):
    n= int(input("Enter a Number: "))
    list.append(n)

def elmn(list):
    for el in list:
        print(el, end = " ")

elmn(list)