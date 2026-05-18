# 72: Number Pattern:
# 1
# 22
# 333
# 4444
n= int(input("Enter Number of rows:" ))
for i in range(1,n+1):
    for j in range(i):
        print(i, end= " ")
    print()
    