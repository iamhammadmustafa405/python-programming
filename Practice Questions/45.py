# 45: Star Pattern (Increasing Stars)
n= int(input("Enter Number of rows: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*", end= " ")
        j+=1
    print()
    i+=1