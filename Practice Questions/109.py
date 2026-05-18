# # 109: Read a file and print only those lines that contain a specific word (e.g., "Python").
with open("practice.txt", "r") as f:
    for line in f:
        if "Python" in line:
            print(line.strip())