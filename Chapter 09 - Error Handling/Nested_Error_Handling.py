# # Nested `try-except` Blocks in Python

# **Nested `try-except`** means putting one `try-except` block **inside another `try` or `except` block**.

# Think of it like **two safety nets**:

# * Outer `try-except` → handles bigger/general errors
# * Inner `try-except` → handles a specific error inside it

# ---

# ## 1. Basic Example

# ```python
# try:
#     print("Outer try")

#     try:
#         x = 10 / 0
#     except ZeroDivisionError:
#         print("Inner: Cannot divide by zero")

# except:
#     print("Outer: Some error occurred")
# ```

# ### Output:

# ```text
# Outer try
# Inner: Cannot divide by zero
# ```

# Why doesn't the outer `except` run?

# Because the **inner `except` already handled the error**.

# Think:

# ```text
# Outer try
#    |
#    └── Inner try
#           |
#           └── Error occurs
#                  |
#                  ↓
#           Inner except handles it
# ```

# ---

# # 2. Why use Nested `try-except`?

# Suppose you have a program doing several things:

# ```python
# try:
#     # Big operation

#     try:
#         # Small operation
#     except:
#         # Handle small error

# except:
#     # Handle bigger error
# ```

# The inner block lets you handle an error **locally**, without stopping the whole outer operation.

# ---

# # 3. Example with Input

# ```python
# try:
#     name = input("Enter your name: ")

#     try:
#         age = int(input("Enter your age: "))
#         print("Age:", age)

#     except ValueError:
#         print("Age must be a number")

#     print("Hello", name)

# except:
#     print("Something went wrong")
# ```

# If the user enters:

# ```text
# Hammad
# abc
# ```

# Output:

# ```text
# Age must be a number
# Hello Hammad
# ```

# The inner `except` catches the `ValueError`.

# ---

# # 4. `try` inside `except`

# You can also put a `try` inside an `except`.

# ```python
# try:
#     x = int("abc")

# except ValueError:
#     print("First error occurred")

#     try:
#         y = 10 / 0
#     except ZeroDivisionError:
#         print("Second error occurred")
# ```

# Output:

# ```text
# First error occurred
# Second error occurred
# ```

# Structure:

# ```text
# try
#  ↓
# Error
#  ↓
# except
#  ↓
#    try
#     ↓
#    Error
#     ↓
#    except
# ```

# ---

# # 5. Multiple Levels of Nesting

# You can technically nest several levels:

# ```python
# try:
#     print("Level 1")

#     try:
#         print("Level 2")

#         try:
#             print("Level 3")

#             x = 10 / 0

#         except ZeroDivisionError:
#             print("Level 3 handled")

#     except:
#         print("Level 2 handled")

# except:
#     print("Level 1 handled")
# ```

# Output:

# ```text
# Level 1
# Level 2
# Level 3
# Level 3 handled
# ```

# The **closest matching `except`** handles the error.

# ---

# # 6. What if Inner `except` Doesn't Handle It?

# This is very important.

# ```python
# try:
#     print("Outer try")

#     try:
#         x = int("hello")

#     except ZeroDivisionError:
#         print("Inner handled")

# except ValueError:
#     print("Outer handled")
# ```

# Output:

# ```text
# Outer try
# Outer handled
# ```

# Why?

# The inner block has:

# ```python
# except ZeroDivisionError:
# ```

# But the actual error is:

# ```python
# ValueError
# ```

# So the inner `except` **doesn't match**.

# Python then looks at the outer `except`.

# ```text
# ValueError occurs
#        ↓
# Inner except?
#        ↓
# No ❌
#        ↓
# Outer except?
#        ↓
# Yes ✅
#        ↓
# Handle error
# ```

# ---

# # 7. Nested `try-except` with `finally`

# You can also use `finally`.

# ```python
# try:
#     print("Outer try")

#     try:
#         x = 10 / 0

#     except ZeroDivisionError:
#         print("Inner except")

#     finally:
#         print("Inner finally")

# except:
#     print("Outer except")

# finally:
#     print("Outer finally")
# ```

# Output:

# ```text
# Outer try
# Inner except
# Inner finally
# Outer finally
# ```

# Remember:

# **`finally` normally runs whether an exception occurs or not.**

# ---

# # 8. Real-Life Example

# Imagine a program opening a file and then processing its contents.

# ```python
# try:
#     file = open("data.txt")

#     try:
#         number = int(file.readline())
#         print(number)

#     except ValueError:
#         print("File contains invalid number")

#     finally:
#         file.close()

# except FileNotFoundError:
#     print("File does not exist")
# ```

# Here:

# ### Outer `try`

# Handles:

# ```python
# FileNotFoundError
# ```

# ### Inner `try`

# Handles:

# ```python
# ValueError
# ```

# ### Inner `finally`

# Makes sure:

# ```python
# file.close()
# ```

# is executed.

# ---

# # 9. Nested vs Multiple `except`

# Don't confuse these:

# ### Multiple `except`

# ```python
# try:
#     x = int(input())
# except ValueError:
#     print("Invalid number")
# except TypeError:
#     print("Type error")
# ```

# There is **one `try`** and multiple `except`s.

# ### Nested `try`

# ```python
# try:
#     try:
#         x = int(input())
#     except ValueError:
#         print("Invalid number")
# except:
#     print("Other error")
# ```

# There are **two `try` blocks**, one inside another.

# ---

# # 10. Easy Rule to Remember

# Think of nested `try-except` like this:

# ```text
# OUTER TRY
# │
# ├── INNER TRY
# │   │
# │   ├── Error
# │   │
# │   └── Inner EXCEPT → handles it if it matches
# │
# └── Outer EXCEPT → handles it if inner doesn't
# ```

# ### Most important concept:

# > **Python first looks for a matching `except` in the current/inner `try`. If it isn't handled there, the exception can propagate outward to an enclosing `try-except`.**

# Nested `try-except` is useful when **different parts of a program need different error-handling behavior**.
