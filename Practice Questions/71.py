# 71: Number Pattern: 
# 1
# 12
# 123
# 1234
n= int(input("Enter Number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end= " ")
    print()