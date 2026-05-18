# 43: Star Pattern (Pyramid)
n= int(input("Enter the Number of rows: "))
i=1
while i<=n:
    # Spaces Printing..
    space=1
    while space <= n-i:
        print(" ", end= " ")
        space +=1
    
    # Stars Printing....
    star =1
    while star<= 2*i-1:
        print("*",end= " ")
        star+=1
    print()
    i+=1
print("This is the Pyramid Astersik Pattern!")
