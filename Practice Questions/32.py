# 32: Count how many numbers between 1 and n are divisible by 3.
n= int(input("Enter a Number: "))
z=1
count=0
while z<=n:
    if z%3==0:
        count+=1
    z+=1
print(f"{count} Numbers are Divisible by 3.")