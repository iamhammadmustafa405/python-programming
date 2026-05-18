# 58: Count the number of vowels in a string.
str= input("Enter your string: ")
vowels= ["a","e","i","o","u"]
count= 0
for i in str:
    if i in vowels:
        count+=1
print(f"{count} Vowels Found!")