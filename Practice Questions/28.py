# 28: Write a Program that checks whether a given number is a palindrome using a while loop.
n= int(input("Enter a Number: "))
z= n
reverse= 0
while n>0:
    digit= n%10
    reverse= reverse*10 + digit # add digit in reverse order
    n= n//10

if z == reverse:
    print(f" Number is a Palindrome")
else: 
    print(f"Number is not a palindrome")