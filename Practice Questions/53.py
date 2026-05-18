# 53: Print the multiplication table of a given number.
n= int(input("Enter the Number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")