# 103:  Search in the file if the any word exists or not.
word= input("Enter the word you want to find in the file: ")
with open("practice.txt","r") as f:
    data = f.read()
    if word in data:
        print("The Word is found.")
    else:
        print("No, there is no such word in this file")
        