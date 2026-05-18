#41: Stars Pattern
n= int(input("Enter Number of rows: "))
i=1
while i<=n:
    j=i
    while j<=i:
        print(j * "*")
        j+=1
    i+=1