# 47: Search for a number x using while loop in the tuple:
num= (1,4,9,16,25,36,49,64,81,100,64)
x= int(input("Enter the Number from the tuple that you want check its index: "))
i=0
while i<len(num):
    if num[i] == x:
        print(f"The Number is found at Index {i}")
        break
    else:
        print("finding....")
    i+=1
print("End of Code.")