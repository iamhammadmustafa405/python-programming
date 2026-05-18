# 65: ind the sum of all elements in a list.
num=[]
for i in range(1,6):
    n= int(input("Enter a Number: "))
    num.append(n)

sum= 0
for i in num:
    sum+=i
print(f"The Sum of the elements of the list: {sum}")