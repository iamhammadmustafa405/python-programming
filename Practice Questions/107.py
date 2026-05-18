# 107: Write a program to count the number of lines in a file.
with open("practice.txt", "r") as f:
    data = True
    lines =0
    while data:
        data = f.readline()
        if data:
            lines +=1
print(f"There are {lines} lines in this file.")