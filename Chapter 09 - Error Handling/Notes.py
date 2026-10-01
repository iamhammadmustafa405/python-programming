# # Error Handling in Python — Full /EL10

# **Error handling** means dealing with problems that happen while your Python program is running, so the program can respond properly instead of suddenly crashing.

# ---

# # 1. What is an Error?

# An error is a problem in a program.

# For example:

# ```python
# print(10 / 0)
# ```

# Python cannot divide by zero.

# It gives:

# ```text
# ZeroDivisionError
# ```

# ---

# # 2. Types of Errors in Python

# There are mainly **three categories** you should know.

# ### 1. Syntax Error

# You wrote Python code incorrectly.

# ```python
# if x > 5
#     print(x)
# ```

# Missing `:`.

# ```text
# SyntaxError
# ```

# ---

# ### 2. Runtime Error / Exception

# The syntax is correct, but something goes wrong **while the program runs**.

# ```python
# x = 10 / 0
# ```

# ```text
# ZeroDivisionError
# ```

# Another example:

# ```python
# numbers = [10, 20, 30]

# print(numbers[5])
# ```

# ```text
# IndexError
# ```

# ---

# ### 3. Logical Error

# The program runs, but gives the **wrong answer**.

# ```python
# a = 10
# b = 5

# print(a - b)
# ```

# If you wanted addition, Python doesn't know that.

# Output:

# ```text
# 5
# ```

# No Python error occurs, but your logic is wrong.

# ---

# # 3. What is an Exception?

# An **exception** is an error that occurs while the program is running.

# Examples:

# ```text
# ZeroDivisionError
# ValueError
# TypeError
# IndexError
# KeyError
# FileNotFoundError
# NameError
# ```

# Python allows us to **catch and handle** these exceptions.

# ---

# # 4. `try` and `except`

# The basic structure is:

# ```python
# try:
#     # risky code
# except:
#     # what to do if an error occurs
# ```

# Example:

# ```python
# try:
#     print(10 / 0)
# except:
#     print("Something went wrong")
# ```

# Output:

# ```text
# Something went wrong
# ```

# Instead of crashing, Python runs the `except` block.

# ---

# # 5. Why Use `try-except`?

# Without error handling:

# ```python
# num = int(input("Enter a number: "))
# print(100 / num)
# ```

# If the user enters:

# ```text
# abc
# ```

# Python crashes with:

# ```text
# ValueError
# ```

# If the user enters:

# ```text
# 0
# ```

# Python crashes with:

# ```text
# ZeroDivisionError
# ```

# We can handle these problems.

# ```python
# try:
#     num = int(input("Enter a number: "))
#     print(100 / num)

# except:
#     print("Invalid input")
# ```

# ---

# # 6. Catching a Specific Exception

# It is better to specify the type of error.

# ```python
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Please enter a number")
# ```

# If the user enters:

# ```text
# abc
# ```

# Output:

# ```text
# Please enter a number
# ```

# ---

# # 7. Multiple `except` Blocks

# You can handle different errors differently.

# ```python
# try:
#     a = int(input("Enter number: "))
#     print(100 / a)

# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")
# ```

# For example:

# ```text
# abc → ValueError
# 0   → ZeroDivisionError
# ```

# ---

# # 8. `except Exception`

# You can catch most ordinary runtime exceptions using:

# ```python
# except Exception:
# ```

# Example:

# ```python
# try:
#     x = 10 / 0

# except Exception:
#     print("An error occurred")
# ```

# ### Better: see the error

# ```python
# try:
#     x = 10 / 0

# except Exception as e:
#     print(e)
# ```

# Output:

# ```text
# division by zero
# ```

# Here:

# ```python
# as e
# ```

# stores the exception object in `e`.

# You can also see its type:

# ```python
# try:
#     x = 10 / 0

# except Exception as e:
#     print(type(e))
#     print(e)
# ```

# ---

# # 9. `else`

# `else` runs **only when no exception occurs**.

# Structure:

# ```python
# try:
#     # risky code

# except:
#     # error

# else:
#     # no error
# ```

# Example:

# ```python
# try:
#     num = int(input("Enter number: "))

# except ValueError:
#     print("Invalid number")

# else:
#     print("You entered:", num)
# ```

# If user enters:

# ```text
# 25
# ```

# Output:

# ```text
# You entered: 25
# ```

# If user enters:

# ```text
# abc
# ```

# Output:

# ```text
# Invalid number
# ```

# ### Easy rule

# ```text
# try    → try this
# except → if error happens
# else   → if NO error happens
# ```

# ---

# # 10. `finally`

# `finally` **always runs**, whether an error occurs or not.

# ```python
# try:
#     print(10 / 2)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Program finished")
# ```

# Output:

# ```text
# 5.0
# Program finished
# ```

# Even if an error occurs:

# ```python
# try:
#     print(10 / 0)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Program finished")
# ```

# Output:

# ```text
# Cannot divide by zero
# Program finished
# ```

# ### Easy rule

# ```text
# try     → try
# except  → error
# else    → no error
# finally → always
# ```

# ---

# # 11. Complete Structure

# You can use all four:

# ```python
# try:
#     # risky code

# except SomeError:
#     # handle error

# else:
#     # runs if no error

# finally:
#     # always runs
# ```

# Example:

# ```python
# try:
#     num = int(input("Enter number: "))
#     result = 100 / num

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)

# finally:
#     print("Done")
# ```

# ---

# # 12. Common Python Exceptions

# These are important:

# | Exception             | Meaning                            |
# | --------------------- | ---------------------------------- |
# | `SyntaxError`         | Invalid Python syntax              |
# | `NameError`           | Variable/name doesn't exist        |
# | `TypeError`           | Wrong type of operation            |
# | `ValueError`          | Correct type but invalid value     |
# | `ZeroDivisionError`   | Division by zero                   |
# | `IndexError`          | Index doesn't exist                |
# | `KeyError`            | Dictionary key doesn't exist       |
# | `FileNotFoundError`   | File doesn't exist                 |
# | `AttributeError`      | Object doesn't have that attribute |
# | `ImportError`         | Import problem                     |
# | `ModuleNotFoundError` | Module cannot be found             |

# ---

# # 13. `ValueError` vs `TypeError`

# This is very important.

# ### ValueError

# The **type is correct**, but the value is inappropriate.

# ```python
# int("hello")
# ```

# `"hello"` is a string, which `int()` accepts as a type, but it cannot convert this particular value.

# ```text
# ValueError
# ```

# ### TypeError

# The **type itself is inappropriate**.

# ```python
# "10" + 5
# ```

# Python cannot add a string and an integer.

# ```text
# TypeError
# ```

# ### Remember:

# > **ValueError → wrong value**

# > **TypeError → wrong type**

# ---

# # 14. Getting the Error Message

# Use:

# ```python
# except Exception as e:
#     print(e)
# ```

# Example:

# ```python
# try:
#     print(10 / 0)

# except Exception as e:
#     print("Error:", e)
# ```

# Output:

# ```text
# Error: division by zero
# ```

# ---

# # 15. Getting the Error Type

# ```python
# try:
#     print(10 / 0)

# except Exception as e:
#     print(type(e))
# ```

# Output:

# ```text
# <class 'ZeroDivisionError'>
# ```

# You can also use:

# ```python
# print(type(e).__name__)
# ```

# Output:

# ```text
# ZeroDivisionError
# ```

# ---

# # 16. Raising Your Own Exception — `raise`

# Python allows you to create an exception yourself.

# Use:

# ```python
# raise
# ```

# Example:

# ```python
# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")
# ```

# Output:

# ```text
# ValueError: Age cannot be negative
# ```

# You're basically telling Python:

# > "This situation is not acceptable, so raise an error."

# ---

# # 17. `raise` with User Input

# ```python
# age = int(input("Enter your age: "))

# if age < 0:
#     raise ValueError("Age cannot be negative")

# print("Age:", age)
# ```

# If the user enters:

# ```text
# -10
# ```

# Python raises:

# ```text
# ValueError: Age cannot be negative
# ```

# ---

# # 18. Creating Your Own Exception

# You can create a custom exception using a class.

# ```python
# class AgeError(Exception):
#     pass
# ```

# Then:

# ```python
# age = -5

# if age < 0:
#     raise AgeError("Invalid age")
# ```

# Output:

# ```text
# AgeError: Invalid age
# ```

# This is called a **custom exception**.

# ---

# # 19. Handling Your Custom Exception

# ```python
# class AgeError(Exception):
#     pass


# try:
#     age = -5

#     if age < 0:
#         raise AgeError("Age cannot be negative")

# except AgeError as e:
#     print(e)
# ```

# Output:

# ```text
# Age cannot be negative
# ```

# ---

# # 20. `assert`

# Python also has `assert`.

# It is used to check whether something is true.

# ```python
# age = 20

# assert age >= 18
# ```

# No error because:

# ```text
# 20 >= 18 → True
# ```

# But:

# ```python
# age = 15

# assert age >= 18
# ```

# Python raises:

# ```text
# AssertionError
# ```

# You can add a message:

# ```python
# age = 15

# assert age >= 18, "Age must be 18 or older"
# ```

# Output:

# ```text
# AssertionError: Age must be 18 or older
# ```

# ### Important

# `assert` is mainly useful for **debugging and internal assumptions**, not as your normal method for validating user input.

# ---

# # 21. Nested `try-except`

# You can put one `try` inside another.

# ```python
# try:
#     print("Outer try")

#     try:
#         print(10 / 0)

#     except ZeroDivisionError:
#         print("Inner error")

# except:
#     print("Outer error")
# ```

# Output:

# ```text
# Outer try
# Inner error
# ```

# The inner `except` handles the error.

# ---

# # 22. Exception Hierarchy

# Python exceptions are organized like a family tree.

# Simplified:

# ```text
# BaseException
# │
# ├── Exception
# │   │
# │   ├── ArithmeticError
# │   │   └── ZeroDivisionError
# │   │
# │   ├── LookupError
# │   │   ├── IndexError
# │   │   └── KeyError
# │   │
# │   ├── ValueError
# │   ├── TypeError
# │   ├── NameError
# │   └── ...
# │
# ├── KeyboardInterrupt
# └── SystemExit
# ```

# This is why:

# ```python
# except Exception:
# ```

# can catch many normal program exceptions.

# ---

# # 23. Order of `except` Matters

# Consider:

# ```python
# try:
#     x = 10 / 0

# except Exception:
#     print("General error")

# except ZeroDivisionError:
#     print("Cannot divide by zero")
# ```

# The second `except` will never be reached because `ZeroDivisionError` is already covered by `Exception`.

# Better:

# ```python
# try:
#     x = 10 / 0

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except Exception:
#     print("Some other error")
# ```

# ### Rule

# Put:

# ```text
# specific exceptions
#         ↓
# general exceptions
# ```

# ---

# # 24. Handling Multiple Exceptions Together

# If you want the same response for multiple errors:

# ```python
# try:
#     x = int(input("Enter: "))
#     print(100 / x)

# except (ValueError, ZeroDivisionError):
#     print("Invalid input")
# ```

# Both errors are handled by the same `except`.

# ---

# # 25. `try-except` with Files

# Error handling is very useful with files.

# ```python
# try:
#     file = open("data.txt", "r")
#     data = file.read()

# except FileNotFoundError:
#     print("File does not exist")

# finally:
#     print("Finished")
# ```

# If `data.txt` doesn't exist:

# ```text
# File does not exist
# Finished
# ```

# For file handling, Python's `with` statement is generally preferred because it automatically handles closing the file.

# ```python
# try:
#     with open("data.txt", "r") as file:
#         data = file.read()

# except FileNotFoundError:
#     print("File not found")
# ```

# ---

# # 26. Re-raising an Exception

# Sometimes you catch an error but want to send it upward again.

# Use:

# ```python
# raise
# ```

# Example:

# ```python
# try:
#     x = 10 / 0

# except ZeroDivisionError:
#     print("Error found")
#     raise
# ```

# Output includes:

# ```text
# Error found
# ```

# followed by the original exception traceback.

# This is useful when you want to **log or inspect an error but still let higher-level code handle it**.

# ---

# # 27. Exception Chaining

# Python can show that one exception happened because of another.

# ```python
# try:
#     number = int("abc")

# except ValueError as e:
#     raise RuntimeError("Could not process number") from e
# ```

# Here:

# ```text
# ValueError
#      ↓
# RuntimeError
# ```

# The `from e` tells Python:

# > "This new error happened because of the previous error."

# ---

# # 28. `finally` and `return`

# `finally` runs even when a function returns.

# ```python
# def test():
#     try:
#         return 10
#     finally:
#         print("Finally runs")


# print(test())
# ```

# Output:

# ```text
# Finally runs
# 10
# ```

# The `finally` block runs **before the function actually returns**.

# ---

# # 29. What NOT to Do

# Avoid this when possible:

# ```python
# try:
#     # everything
# except:
#     pass
# ```

# Why?

# Because it hides the error.

# Example:

# ```python
# try:
#     x = 10 / 0
# except:
#     pass

# print("Program continues")
# ```

# Output:

# ```text
# Program continues
# ```

# But you don't know what went wrong.

# Better:

# ```python
# try:
#     x = 10 / 0

# except ZeroDivisionError as e:
#     print("Error:", e)
# ```

# ---

# # 30. Real-World Example

# Let's make a simple calculator:

# ```python
# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))

#     result = a / b

# except ValueError:
#     print("Please enter numbers only.")

# except ZeroDivisionError:
#     print("You cannot divide by zero.")

# else:
#     print("Result:", result)

# finally:
#     print("Calculator finished.")
# ```

# ### If user enters:

# ```text
# 10
# 2
# ```

# Output:

# ```text
# Result: 5.0
# Calculator finished.
# ```

# ### If user enters:

# ```text
# abc
# 2
# ```

# Output:

# ```text
# Please enter numbers only.
# Calculator finished.
# ```

# ### If user enters:

# ```text
# 10
# 0
# ```

# Output:

# ```text
# You cannot divide by zero.
# Calculator finished.
# ```

# ---

# # 31. The Complete Picture

# Remember this structure:

# ```text
#                  ERROR HANDLING
#                        │
#           ┌────────────┴────────────┐
#           │                         │
#        Errors                  Exceptions
#           │                         │
#    Syntax/Logical          Runtime problems
#                                   │
#                            try / except
#                                   │
#                     ┌─────────────┼─────────────┐
#                     │             │             │
#                   except         else        finally
#                     │             │             │
#                  error         no error       always
# ```

# And these keywords are the most important:

# ```python
# try
# except
# else
# finally
# raise
# assert
# ```

# ### One-line memory trick

# > **`try` = try something, `except` = handle error, `else` = no error, `finally` = always, `raise` = create/throw error, `assert` = check an assumption.**
