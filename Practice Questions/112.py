# # 112: Write a program to replace a specific word in a file with another word.
# old = input("Enter the Word You want to replace:")
# new = input("Enter the new word: ")

# with open("words.txt", "r") as f:
#     data = f.read()
#     updated_data= data.replace(old, new)

# with open("words.txt", "w") as f:
#     f.write(updated_data)

# Advanced improvement (case-insensitive replacement)

# Your current code is case-sensitive. For example:

# "Python" ≠ "python"

# Improved version:

import re

old = input("Enter the word you want to replace: ")
new = input("Enter the new word: ")

with open("words.txt", "r") as f:
    data = f.read()

updated_data = re.sub(old, new, data, flags=re.IGNORECASE)

with open("words.txt", "w") as f:
    f.write(updated_data)