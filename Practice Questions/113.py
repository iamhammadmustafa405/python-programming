# 113: Write a program to remove blank lines from a file.
with open("words.txt", "r") as f:
    lines = f.readlines()
with open("words.txt", "w") as f:
    for line in lines:
        if line.strip() != "":
            f.write(line)

    
    