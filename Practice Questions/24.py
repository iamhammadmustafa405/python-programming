# 24: write a Program to count the number of digits in a given number using a while loop.
n= int(input("Enter a Number: "))
count= 0
while n>0:
    n= n//10 # Skips the last digit
    count +=1
print(f"Digits: {count}")