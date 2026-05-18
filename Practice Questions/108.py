# 108: Write a program to count the number of words in a file.

# with open("words.txt", "r") as f:
#     data= f.read()
#     words= data.split(" ")
#     count= 0
#     for i in words:
#         count+=1
# print(f"There are {count} words in this file.")

# 2nd Method:

with open("words.txt", "r") as f:
    data= f.read()
    words= data.split()
    count= len(words)
    
print(f"There are {count} words in this file.")
