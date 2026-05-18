# File Handling...
# f = open("C:\Hammad Mustafa\Artificial Intelligence & Data Science\Python Programming\Chapter 07 - File I-O\demo.txt", "r")
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f= open("C:\Hammad Mustafa\Artificial Intelligence & Data Science\Python Programming\Chapter 07 - File I-O\demo.txt", "w")
# f.write("Hello My age is 18 years old.") # it overwrites data in the file
# f.close()

# f= open("C:\Hammad Mustafa\Artificial Intelligence & Data Science\Python Programming\Chapter 07 - File I-O\demo.txt", "a")
# f.write("\n I am learning Python Programming.")
# f.write("\n I am also learining Sql")
# f.close()


# Notes:-


# 📂 Basic Idea
# When you open a file using:
# f = open("file.txt", "mode")
# 👉 The mode tells Python:


# What you want to do (read/write/etc.)


# And how you want to do it



# 📖 1. Read Mode (r)
# open("file.txt", "r")
# ✔ Used to read data
# ✔ File must exist
# ❌ Error if file does not exist
# 👉 Example:
# f = open("file.txt", "r")print(f.read())

# ✍️ 2. Write Mode (w)
# open("file.txt", "w")
# ✔ Used to write data
# ✔ Creates file if not exists
# ⚠ Deletes old data (overwrite)
# 👉 Example:
# f = open("file.txt", "w")f.write("Hello")

# ➕ 3. Append Mode (a)
# open("file.txt", "a")
# ✔ Adds data at the end
# ✔ Creates file if not exists
# ❌ Does NOT delete old data
# 👉 Example:
# f = open("file.txt", "a")f.write("New line")

# 🔄 4. Read + Write Mode (r+)
# open("file.txt", "r+")
# ✔ Read + Write both
# ✔ File must exist
# ❌ Does NOT delete data automatically

# 🔄 5. Write + Read Mode (w+)
# open("file.txt", "w+")
# ✔ Read + Write
# ✔ Creates file if not exists
# ⚠ Deletes old data

# 🔄 6. Append + Read Mode (a+)
# open("file.txt", "a+")
# ✔ Read + Append
# ✔ Creates file if not exists
# ✔ Writing always at end

# 🧾 7. Text Mode (t)
# open("file.txt", "rt")
# ✔ Default mode
# ✔ Works with normal text
# 👉 You usually don’t write t because it is already default.

# 🧱 8. Binary Mode (b)
# open("file.txt", "rb")
# ✔ Used for images, videos, PDFs
# ✔ Works with binary data
# 👉 Example:
# f = open("image.jpg", "rb")

# 🔀 Combining Modes
# You can combine modes like:
# ModeMeaningrbRead binarywbWrite binaryabAppend binaryr+bRead + write binary

# 🧠 Easy Summary Table
# ModeUseFile Exists?Old DatarReadMust existSafewWriteNot requiredDeletedaAppendNot requiredSafer+Read + WriteMust existSafew+Write + ReadNot requiredDeleteda+Append + ReadNot requiredSafe

# ⚠️ Important Tips


# Always close file:


# f.close()


# Best way (automatic close):


# with open("file.txt", "r") as f:    print(f.read())

# If you want, I can give:


# Practice questions


# Common mistakes (like the one you had earlier)


# Real-life examples (projects)


# 🌊 1. Basic Stream Idea (Flow of Data)
# [ FILE ]  ───────▶  [ PROGRAM ]
#    📄          (Reading)

# 👉 Data is flowing from file → program
# 👉 This is called Input Stream

# [ PROGRAM ]  ───────▶  [ FILE ]
#               (Writing)

# 👉 Data is flowing from program → file
# 👉 This is called Output Stream

# 🎬 2. Animation-Style Explanation
# 📥 Reading (Input Stream)
# Step 1:
# FILE:   H e l l o   W o r l d
#          ^
#        cursor

# Step 2:
# Program reads "H"
# Cursor moves →

# Step 3:
# Program reads "e"
# Cursor moves →

# Step 4:
# Program reads "l"
# Cursor moves →

# 👉 Data comes one by one (flowing) like water

# 📤 Writing (Output Stream)
# Program wants to write: "Hi"
# Step 1:
# FILE:   _
#          ^
#        cursor

# Step 2:
# Write "H"
# FILE:   H
#           ^
#         cursor

# Step 3:
# Write "i"
# FILE:   H i
#             ^
#           cursor

# 👉 Data goes step by step into file

# 🎯 3. Pipe Example (Best Visualization)
#       (Reading)

#    📄 FILE
#      │
#      │   (data flows like water)
#      ▼
#    💻 PROGRAM
#       (Writing)

#    💻 PROGRAM
#      │
#      │   (data flows like water)
#      ▼
#    📄 FILE
# 📍 4. Cursor (Very Important)

# Cursor = pointer showing current position

# FILE:  H e l l o
#         ^
#      cursor
# read() → moves cursor forward
# write() → writes at cursor position
# ⚠️ Real Behavior Example
# f = open("file.txt", "r+")
# f.read(3)
# f.write("X")
# Before:  H e l l o
#            ^

# After read(3):
# Cursor → after "Hel"

# Write "X":

# Result: H e l X o
# ✅ Final Understanding
# Stream = flow of data
# Like water in a pipe
# Reading = file → program
# Writing = program → file
# Cursor = controls where data flows next




 # Clear the concept of stream.


# f= open("demo.txt", "r+")
# f.write("No")
# print(f.read())
# f.close() 






# 2. Cursor starts at the end

# So if you try to read immediately, you get nothing.

# 👉 Example:

# f = open("file.txt", "a+")
# print(f.read())   # ❌ empty output

# 3. To read, move cursor to start
# f.seek(0)   # move cursor to beginning
# print(f.read())

# f= open("demo.txt", "a+")
# f.seek(0)  # Bring Cursor to the start/ beginning  of the file.
# print(f.read())




# # With keyword.
# with open("demo.txt","r") as f:
#     print(f.read())



# Deleting a File

import os
os.remove("demo.txt")