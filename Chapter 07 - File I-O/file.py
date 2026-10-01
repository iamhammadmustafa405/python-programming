# # File Handling in Python — Complete Guide

# File handling means **creating, opening, reading, writing, and managing files using Python**.

# Think of a file like a notebook on your computer:

# ```text
# Python program
#      ↓
#    File
#      ↓
# read / write / append
# ```

# ---

# # 1. Opening a File

# Python uses the `open()` function.

# ```python
# file = open("data.txt")
# ```

# General syntax:

# ```python
# open(filename, mode)
# ```

# Example:

# ```python
# file = open("data.txt", "r")
# ```

# Here:

# * `"data.txt"` → file name
# * `"r"` → mode
# * `file` → file object

# ---

# # 2. File Modes

# These are the important modes:

# | Mode  | Meaning      |
# | ----- | ------------ |
# | `"r"` | Read         |
# | `"w"` | Write        |
# | `"a"` | Append       |
# | `"x"` | Create       |
# | `"b"` | Binary       |
# | `"t"` | Text         |
# | `"+"` | Read + Write |

# They can be combined.

# ```text
# r   → read
# w   → write
# a   → append
# x   → create
# rb  → read binary
# wb  → write binary
# r+  → read + write
# w+  → write + read
# a+  → append + read
# ```

# ---

# # 3. `"r"` — Read

# Used to read an existing file.

# ```python
# file = open("data.txt", "r")

# data = file.read()

# print(data)

# file.close()
# ```

# If the file doesn't exist:

# ```text
# FileNotFoundError
# ```

# ---

# # 4. `"w"` — Write

# Used to write data.

# ```python
# file = open("data.txt", "w")

# file.write("Hello Python")

# file.close()
# ```

# Important:

# **`w` can erase existing content.**

# Suppose:

# ```text
# data.txt
# Hello
# World
# ```

# Then:

# ```python
# open("data.txt", "w")
# ```

# and writing:

# ```python
# file.write("Python")
# ```

# results in:

# ```text
# Python
# ```

# The old content is gone.

# ---

# # 5. `"a"` — Append

# Adds data to the **end** of the file.

# ```python
# file = open("data.txt", "a")

# file.write("\nPython")

# file.close()
# ```

# If the file contains:

# ```text
# Hello
# World
# ```

# it becomes:

# ```text
# Hello
# World
# Python
# ```

# It doesn't delete the existing content.

# ---

# # 6. `"x"` — Create

# Creates a **new file**.

# ```python
# file = open("newfile.txt", "x")

# file.write("Hello")

# file.close()
# ```

# If the file already exists:

# ```text
# FileExistsError
# ```

# ---

# # 7. `"b"` — Binary Mode

# Used for binary files such as:

# ```text
# images
# videos
# PDFs
# audio
# executables
# ```

# Example:

# ```python
# file = open("image.jpg", "rb")

# data = file.read()

# file.close()
# ```

# `b` is usually combined with another mode:

# ```python
# "rb"
# "wb"
# "ab"
# ```

# ---

# # 8. `"t"` — Text Mode

# Text mode is the default.

# ```python
# file = open("data.txt", "rt")
# ```

# This is equivalent to:

# ```python
# file = open("data.txt", "r")
# ```

# So:

# ```text
# "r" = "rt"
# ```

# ---

# # 9. `"+"` — Read and Write

# Allows both reading and writing.

# ### `r+`

# ```python
# file = open("data.txt", "r+")
# ```

# Read and write.

# The file must already exist.

# ### `w+`

# ```python
# file = open("data.txt", "w+")
# ```

# Write and read.

# ⚠️ Existing content is erased.

# ### `a+`

# ```python
# file = open("data.txt", "a+")
# ```

# Append and read.

# ---

# # 10. `close()`

# After working with a file, close it.

# ```python
# file = open("data.txt", "r")

# data = file.read()

# file.close()
# ```

# Why?

# Because the operating system has limited resources for open files.

# ---

# # 11. `read()`

# Reads the entire file.

# Suppose:

# ```text
# data.txt

# Hello
# Python
# World
# ```

# ```python
# file = open("data.txt", "r")

# data = file.read()

# print(data)

# file.close()
# ```

# Output:

# ```text
# Hello
# Python
# World
# ```

# ---

# # 12. `read(n)`

# Reads a specific number of characters.

# ```python
# file = open("data.txt", "r")

# print(file.read(5))

# file.close()
# ```

# If the file contains:

# ```text
# Hello Python
# ```

# Output:

# ```text
# Hello
# ```

# ---

# # 13. `readline()`

# Reads **one line**.

# ```python
# file = open("data.txt", "r")

# print(file.readline())

# file.close()
# ```

# Suppose:

# ```text
# Apple
# Banana
# Mango
# ```

# First `readline()`:

# ```text
# Apple
# ```

# Second:

# ```python
# print(file.readline())
# ```

# gives:

# ```text
# Banana
# ```

# ---

# # 14. `readlines()`

# Reads all lines and returns them as a **list**.

# ```python
# file = open("data.txt", "r")

# lines = file.readlines()

# print(lines)

# file.close()
# ```

# Output:

# ```python
# ['Apple\n', 'Banana\n', 'Mango\n']
# ```

# Notice `\n`.

# It represents a **newline**.

# ---

# # 15. Reading Using a Loop

# This is commonly used for large files.

# ```python
# file = open("data.txt", "r")

# for line in file:
#     print(line)

# file.close()
# ```

# Python reads the file **line by line** instead of loading everything at once.

# ---

# # 16. `write()`

# Writes a string to a file.

# ```python
# file = open("data.txt", "w")

# file.write("Hello")

# file.close()
# ```

# Important:

# `write()` expects a **string**.

# This won't work directly:

# ```python
# file.write(100)
# ```

# Use:

# ```python
# file.write(str(100))
# ```

# ---

# # 17. `writelines()`

# Writes multiple strings.

# ```python
# file = open("data.txt", "w")

# lines = ["Apple\n", "Banana\n", "Mango\n"]

# file.writelines(lines)

# file.close()
# ```

# Result:

# ```text
# Apple
# Banana
# Mango
# ```

# Important:

# `writelines()` does **not automatically add `\n`**.

# So:

# ```python
# file.writelines(["Apple", "Banana"])
# ```

# produces:

# ```text
# AppleBanana
# ```

# ---

# # 18. `seek()`

# Moves the file pointer.

# Imagine a cursor inside your file:

# ```text
# Hello Python
# ^
# ```

# After reading:

# ```text
# Hello Python
#      ^
# ```

# `seek()` moves it.

# ```python
# file.seek(0)
# ```

# moves the pointer back to the beginning.

# Example:

# ```python
# file = open("data.txt", "r")

# print(file.read(5))

# file.seek(0)

# print(file.read(5))

# file.close()
# ```

# Output:

# ```text
# Hello
# Hello
# ```

# ---

# # 19. `tell()`

# Tells you the current position of the file pointer.

# ```python
# file = open("data.txt", "r")

# print(file.tell())

# file.read(5)

# print(file.tell())

# file.close()
# ```

# Possible output:

# ```text
# 0
# 5
# ```

# So:

# ```text
# tell() → where am I?
# seek() → move me somewhere
# ```

# ---

# # 20. `with open()` — Recommended Way

# Instead of manually closing:

# ```python
# file = open("data.txt", "r")

# data = file.read()

# file.close()
# ```

# Use:

# ```python
# with open("data.txt", "r") as file:
#     data = file.read()

# print(data)
# ```

# Python automatically closes the file.

# This is the **preferred way**.

# ---

# # 21. Writing with `with`

# ```python
# with open("data.txt", "w") as file:
#     file.write("Hello Python")
# ```

# No need for:

# ```python
# file.close()
# ```

# ---

# # 22. File Paths

# You can specify a path.

# ### Relative path

# ```python
# open("data.txt")
# ```

# Means the file is relative to your current working directory.

# You can also use:

# ```python
# open("data/data.txt")
# ```

# ### Absolute path

# Windows:

# ```python
# open(r"C:\Users\Hammad\Documents\data.txt")
# ```

# The `r` before the string means **raw string**.

# It prevents backslashes from being interpreted as escape sequences.

# ---

# # 23. `encoding`

# When working with text files, you can specify encoding.

# ```python
# with open("data.txt", "r", encoding="utf-8") as file:
#     data = file.read()
# ```

# UTF-8 supports a huge range of characters.

# For example:

# ```text
# English
# اردو
# 中文
# العربية
# ```

# ---

# # 24. `newline`

# You can control newline handling.

# ```python
# with open("data.txt", "r", newline="") as file:
#     data = file.read()
# ```

# This becomes particularly useful when working with **CSV files**.

# ---

# # 25. File Object Methods

# The important methods are:

# ```text
# read()
# readline()
# readlines()

# write()
# writelines()

# seek()
# tell()

# close()
# ```

# You can also use:

# ```python
# file.readable()
# file.writable()
# ```

# Example:

# ```python
# with open("data.txt", "r") as file:
#     print(file.readable())
#     print(file.writable())
# ```

# Output:

# ```text
# True
# False
# ```

# ---

# # 26. `flush()`

# Forces buffered data to be written.

# ```python
# file = open("data.txt", "w")

# file.write("Hello")

# file.flush()

# file.close()
# ```

# Usually, you don't need to call `flush()` manually when using `with`.

# ---

# # 27. `fileno()`

# Returns the file descriptor assigned by the operating system.

# ```python
# with open("data.txt", "r") as file:
#     print(file.fileno())
# ```

# Example output:

# ```text
# 3
# ```

# The exact number can vary.

# ---

# # 28. `isatty()`

# Checks whether the file is connected to a terminal.

# ```python
# with open("data.txt", "r") as file:
#     print(file.isatty())
# ```

# Usually:

# ```text
# False
# ```

# ---

# # 29. `readable()` and `writable()`

# ```python
# with open("data.txt", "r") as file:
#     print(file.readable())
#     print(file.writable())
# ```

# Output:

# ```text
# True
# False
# ```

# ---

# # 30. `seekable()`

# Checks whether the file supports changing the file position.

# ```python
# with open("data.txt", "r") as file:
#     print(file.seekable())
# ```

# Usually:

# ```text
# True
# ```

# ---

# # 31. File Exceptions

# File operations can produce errors.

# ### File doesn't exist

# ```python
# open("abc.txt", "r")
# ```

# Result:

# ```text
# FileNotFoundError
# ```

# ### File already exists with `x`

# ```python
# open("abc.txt", "x")
# ```

# Result:

# ```text
# FileExistsError
# ```

# ### Permission problem

# ```text
# PermissionError
# ```

# ### Invalid path

# ```text
# OSError
# ```

# ---

# # 32. Handling Errors

# Use `try-except`.

# ```python
# try:
#     with open("data.txt", "r") as file:
#         data = file.read()

# except FileNotFoundError:
#     print("File does not exist.")
# ```

# This prevents your program from crashing when the file isn't found.

# ---

# # 33. `os` Module

# Python's `os` module lets you work with files and directories.

# ```python
# import os
# ```

# ### Check whether a file exists

# ```python
# os.path.exists("data.txt")
# ```

# ### Check whether it is a file

# ```python
# os.path.isfile("data.txt")
# ```

# ### Check whether it is a directory

# ```python
# os.path.isdir("data")
# ```

# ---

# # 34. Delete a File

# ```python
# import os

# os.remove("data.txt")
# ```

# ⚠️ This permanently removes the file.

# Check first:

# ```python
# if os.path.exists("data.txt"):
#     os.remove("data.txt")
# ```

# ---

# # 35. Create a Directory

# ```python
# import os

# os.mkdir("data")
# ```

# Creates:

# ```text
# data/
# ```

# ---

# # 36. Create Nested Directories

# ```python
# os.makedirs("data/python/files")
# ```

# Creates all necessary directories.

# ---

# # 37. Delete an Empty Directory

# ```python
# os.rmdir("data")
# ```

# The directory must be empty.

# ---

# # 38. Rename a File

# ```python
# os.rename("old.txt", "new.txt")
# ```

# ---

# # 39. Current Working Directory

# ```python
# import os

# print(os.getcwd())
# ```

# Example:

# ```text
# D:\Artificial Intelligence (AI)\Python
# ```

# This tells you where Python is currently working.

# ---

# # 40. Change Working Directory

# ```python
# os.chdir("D:\\Python")
# ```

# Now Python's working directory changes.

# ---

# # 41. `pathlib` — Modern Way

# Python also has the `pathlib` module.

# ```python
# from pathlib import Path
# ```

# Create a path:

# ```python
# path = Path("data.txt")
# ```

# Check existence:

# ```python
# print(path.exists())
# ```

# Check file:

# ```python
# print(path.is_file())
# ```

# Check directory:

# ```python
# print(path.is_dir())
# ```

# ---

# # 42. Reading with `pathlib`

# ```python
# from pathlib import Path

# path = Path("data.txt")

# data = path.read_text()

# print(data)
# ```

# ---

# # 43. Writing with `pathlib`

# ```python
# from pathlib import Path

# path = Path("data.txt")

# path.write_text("Hello Python")
# ```

# ---

# # 44. File Encoding with `pathlib`

# ```python
# path.write_text("Hello", encoding="utf-8")
# ```

# Reading:

# ```python
# data = path.read_text(encoding="utf-8")
# ```

# ---

# # 45. Important File Handling Concepts

# You should understand these especially well:

# ```text
# open()
#   ↓
# mode
#   ↓
# read / write
#   ↓
# file pointer
#   ↓
# seek() / tell()
#   ↓
# close()
# ```

# ### Modes

# ```text
# r   → read
# w   → write / overwrite
# a   → append
# x   → create
# b   → binary
# t   → text
# +   → read + write
# ```

# ### Main methods

# ```text
# read()
# readline()
# readlines()

# write()
# writelines()

# seek()
# tell()

# close()
# flush()
# ```

# ### Recommended pattern

# ```python
# with open("data.txt", "r", encoding="utf-8") as file:
#     data = file.read()

# print(data)
# ```

# This is the pattern you should use most of the time.

# ### One-line memory trick

# > **`r` reads, `w` wipes and writes, `a` adds, `x` creates, `b` handles bytes, `+` adds reading/writing.**
