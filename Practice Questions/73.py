# 73: print Pyramid: 
n= int(input("Enter Number of rows: "))
for i in range(1,n+1):
    # Space Printing....
    for j in range(n-i):
        print(" ", end= " ")
    # Stars Printing....
    for k in range(2*i-1):
        print("&",end= " ")
    print()