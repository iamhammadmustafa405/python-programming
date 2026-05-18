# 26:Write a Program that using a while loop to find the factorial of the given number.
n= int(input("Enter a Number: "))
fact= 1
count =1
while count<=n:
    fact *= count
    count+=1
print(f"The Factorial of the given number is: {fact}")