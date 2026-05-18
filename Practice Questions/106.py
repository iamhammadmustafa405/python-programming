# 106: Create a file and write your name, age, and city into it. Then read and display the content.
with open("intro.txt", "w") as f:
    f.write("My name is Hammad Mustafa. I am 19  years old. Currently, I am living in Azad Kashmir.")

with open("intro.txt", "r") as f:
    data= f.read()
    print(data)