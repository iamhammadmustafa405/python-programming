# Question - 08: Write a program to check whether a given string is empty or not.
txt= input("Enter text: ")
if len(txt.strip()) == 0: # strip() removes leading and trailing spaces.
    print("It is an empty string.")
else:
    print("It is not an empty string.")