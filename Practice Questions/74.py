# 74:  Check if a number is prime using a for loop.
n= int(input("Enter a Number: "))
for i in range(2,n):
    if n % i == 0:
        print("The Number is Not Prime.")
        break
else:
    print("The Number is Prime.")