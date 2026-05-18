# 67: Reverse a list using a loop (without slicing).
num= []
reverse=[]
for i in range(1,6):
    n= int(input("Enter a Number: "))
    num.append(n)

for i in range(len(num)-1,-1,-1):
    reverse.append(num[i])
print(f"The Reversed list is: {reverse}")