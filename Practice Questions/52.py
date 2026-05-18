# 52: Calculate the sum of numbers from 1 to n (user input).
n= int(input("Enter the Number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)