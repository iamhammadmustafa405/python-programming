# 111: Append data to an existing file and then display the updated content.
with open("data.txt", "a") as f:
    f.write("\nMy Name is Hammad Mustafa.")

with open("data.txt", "r") as f:
    updated_data = f.read()
    print(updated_data)