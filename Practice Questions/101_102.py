# 101: Create a new file in "Practice.txt" using python. add the following data in it.
# hi everyone
# We are learning File I/O
# Using Java
# I like Programming in Java.
# with open("practice.txt", "a") as f:
#     f.write("hi everyone")
#     f.write("\n We are learning File I/O")
#     f.write("\n Using Java")
#     f.write("\n I like Programming in Java.")
#     f.close()

# 102: Write a Function that repalces all occurances of "Java" with "Python" in above file.
def replace(file):
    with open(file, "r") as f:
        data = f.read()
        new_data =  data.replace("Java","Python")
    with open(file,"w") as f:
        f.write(new_data)
    
replace("practice.txt")