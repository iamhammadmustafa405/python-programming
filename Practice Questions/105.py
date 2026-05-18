# 105: From a file containing numbers seperated by comma, print the count of even numbers.
with open("numbers.txt", "r") as f:
    data = f.read()
    count = 0
    nums= data.split(",")
    for i in nums:
        if int(i) % 2 == 0:
            count += 1
print(f"There are {count} Even Numbers in this File.")