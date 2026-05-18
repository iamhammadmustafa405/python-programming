# 110: Write a program to copy the contents of one file into another file.
# with open("practice.txt", "r") as f:
#     data = f.read()

# with open("data.txt", "w") as f:
#     f.write(data)

# line by line targeting
with open("practice.txt", "r") as source:
    with open("data.txt", "w") as target:  # ----> Line by Line Copying Using For Loop 
        for line in source:
            target.write(line)
