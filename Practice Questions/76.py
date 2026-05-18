# 76: search for a number x using for loop in the tuple.
num= (4,5,6,7,2,3,5)
x= 5
idx = 0
for n in num:
    if (n == x):
        print(f"{x} is found at index {idx}")
    idx+=1
