# 21:  Create a program that prints the multiplication table of a number using a while loop.
a= int(input("Enter a Number: "))
count=1
while count<=10:
    print(f"{a} x {count} = {a*count}")
    count+=1