# 54: Count How many numbers between 1-100 are divisible by 3 using for loop.
count=0
for i in range(1,101):
    if i%3 ==0:
        count+=1
print(f"{count} numbers are Divisible by 3")