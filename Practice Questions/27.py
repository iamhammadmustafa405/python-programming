# 27: Use a while loop to find the Fibonacci series upto n terms.
terms= int(input("Enter a Number: "))
a= 0
b=1
count=0
while count<terms:
    print(a)
    next_number= a+b
    a= b
    b= next_number
    count+=1
