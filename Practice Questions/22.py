# 22:  Write a Program to calculate the sum of numbers from 1 to n using a while loop.
n= int(input("Enter a Number: "))
sum= 0
count =1
while count<=n:
    sum += count
    count+=1
print(sum)