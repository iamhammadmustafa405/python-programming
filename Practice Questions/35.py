# 35: Check if a number is prime using a while loop
n= int(input("Enter a Number: "))
count=2
while count<n:
    if n % count== 0:
        print("The Number is Not Prime.")
        break
    count+=1
else:
    print("The Number is Prime")