# 143:File Reader Program (File Handling + finally)
# Write a program that:

# Asks the user for a filename
# Tries to open and read the file

# Requirements:

# Handle:
# FileNotFoundError → if file does not exist
# PermissionError → if access is denied
# Use else to print file content
# Use finally to print: "File operation completed"
# Ensure the file is properly closed (if opened)
try:
    file_name= input("Enter file name: ")
    
    with open(file_name, "r") as f:
        data = f.read()

except FileNotFoundError:
    print("File didn't Exists!")

except Exception as e:
    print(f"Error: {e}")

else:
    print(f"File Content: {data}")
finally:
    print("File operation completed!")