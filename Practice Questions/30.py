# 30: Find the sum of all the even numbers between 1 and n.
n= int(input("Enter a Number: "))
count= 1
sum = 0
while count<=n:
    if count%2 == 0:
        sum+= count
    count+=1
print(f"Sum of even numbers between 1 and {n} is : {sum}")