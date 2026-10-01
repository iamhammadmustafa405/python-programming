# # Functions and Recursion in Python — Full Guide

# A **function** is a reusable block of code that performs a particular task.

# Instead of writing:

# ```python
# print("Hello")
# print("Hello")
# print("Hello")
# ```

# you can create a function once:

# ```python
# def hello():
#     print("Hello")
# ```

# and call it whenever you need:

# ```python
# hello()
# hello()
# hello()
# ```

# ---

# # Part 1 — Functions

# ## 1. Creating a Function

# The basic syntax is:

# ```python
# def function_name():
#     # code
# ```

# Example:

# ```python
# def greet():
#     print("Hello Hammad")
# ```

# The function doesn't run when you define it.

# You need to **call** it:

# ```python
# greet()
# ```

# Output:

# ```text
# Hello Hammad
# ```

# ---

# # 2. Function Call

# Calling means telling Python:

# > "Run this function."

# ```python
# greet()
# ```

# You can call it multiple times:

# ```python
# greet()
# greet()
# greet()
# ```

# ---

# # 3. Parameters

# A **parameter** is a variable written inside the function definition.

# ```python
# def greet(name):
#     print("Hello", name)
# ```

# Here:

# ```text
# name → parameter
# ```

# Call:

# ```python
# greet("Hammad")
# ```

# Output:

# ```text
# Hello Hammad
# ```

# ---

# # 4. Arguments

# The actual value passed to a function is called an **argument**.

# ```python
# greet("Hammad")
# ```

# Here:

# ```text
# name       → parameter
# "Hammad"   → argument
# ```

# Easy distinction:

# > **Parameter = variable in the function definition.**
# > **Argument = actual value passed to the function.**

# ---

# # 5. Multiple Parameters

# ```python
# def add(a, b):
#     print(a + b)
# ```

# Call:

# ```python
# add(10, 20)
# ```

# Output:

# ```text
# 30
# ```

# Here:

# ```text
# a = 10
# b = 20
# ```

# ---

# # 6. `return`

# `return` sends a value **back to the place where the function was called**.

# ```python
# def add(a, b):
#     return a + b
# ```

# Now:

# ```python
# result = add(10, 20)

# print(result)
# ```

# Output:

# ```text
# 30
# ```

# Think:

# ```text
# add(10, 20)
#      ↓
#    function
#      ↓
#     30
#      ↓
#  result
# ```

# ---

# # 7. `print()` vs `return`

# This is very important.

# ### `print()`

# Displays something:

# ```python
# def add(a, b):
#     print(a + b)
# ```

# ### `return`

# Gives the value back:

# ```python
# def add(a, b):
#     return a + b
# ```

# For example:

# ```python
# x = add(5, 3)
# ```

# With `return`:

# ```text
# x = 8
# ```

# With only `print()`:

# ```text
# 8 is displayed
# x = None
# ```

# ---

# # 8. Function Without `return`

# ```python
# def hello():
#     print("Hello")
# ```

# If you do:

# ```python
# x = hello()

# print(x)
# ```

# Output:

# ```text
# Hello
# None
# ```

# Why?

# Because a function without an explicit `return` automatically returns:

# ```python
# None
# ```

# ---

# # 9. Default Parameters

# You can give a parameter a default value.

# ```python
# def greet(name="Hammad"):
#     print("Hello", name)
# ```

# Now:

# ```python
# greet()
# ```

# Output:

# ```text
# Hello Hammad
# ```

# But:

# ```python
# greet("Ali")
# ```

# Output:

# ```text
# Hello Ali
# ```

# The supplied argument replaces the default.

# ---

# # 10. Positional Arguments

# Arguments are matched according to their **position**.

# ```python
# def student(name, age):
#     print(name, age)

# student("Hammad", 19)
# ```

# Python does:

# ```text
# name = "Hammad"
# age = 19
# ```

# ---

# # 11. Keyword Arguments

# You can specify the parameter name.

# ```python
# student(age=19, name="Hammad")
# ```

# The order doesn't matter.

# ```python
# student(name="Hammad", age=19)
# ```

# Both work.

# ---

# # 12. Positional + Keyword Arguments

# You can combine them.

# ```python
# def student(name, age, city):
#     print(name, age, city)

# student("Hammad", age=19, city="Islamabad")
# ```

# Important rule:

# **Positional arguments must come before keyword arguments.**

# Correct:

# ```python
# student("Hammad", age=19)
# ```

# Incorrect:

# ```python
# student(name="Hammad", 19)
# ```

# ---

# # 13. Arbitrary Positional Arguments — `*args`

# Sometimes you don't know how many arguments you'll receive.

# Use:

# ```python
# *args
# ```

# Example:

# ```python
# def add(*numbers):
#     print(numbers)
# ```

# Call:

# ```python
# add(10, 20, 30, 40)
# ```

# Output:

# ```text
# (10, 20, 30, 40)
# ```

# `args` is a **tuple**.

# Therefore:

# ```python
# def add(*numbers):
#     print(type(numbers))
# ```

# Output:

# ```text
# <class 'tuple'>
# ```

# You can loop through it:

# ```python
# def add(*numbers):
#     total = 0

#     for number in numbers:
#         total += number

#     return total
# ```

# Then:

# ```python
# print(add(10, 20, 30))
# ```

# Output:

# ```text
# 60
# ```

# ---

# # 14. Arbitrary Keyword Arguments — `**kwargs`

# For an unknown number of keyword arguments:

# ```python
# def student(**data):
#     print(data)
# ```

# Call:

# ```python
# student(name="Hammad", age=19, city="Islamabad")
# ```

# Output:

# ```text
# {'name': 'Hammad', 'age': 19, 'city': 'Islamabad'}
# ```

# `kwargs` is a **dictionary**.

# ```python
# def student(**data):
#     print(type(data))
# ```

# Output:

# ```text
# <class 'dict'>
# ```

# ---

# # 15. `*args` vs `**kwargs`

# | Syntax     | Stores data in |
# | ---------- | -------------- |
# | `*args`    | Tuple          |
# | `**kwargs` | Dictionary     |

# Example:

# ```python
# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)

# test(10, 20, name="Hammad", age=19)
# ```

# Output:

# ```text
# (10, 20)
# {'name': 'Hammad', 'age': 19}
# ```

# ---

# # 16. Parameter Order

# A common general order is:

# ```python
# def function(
#     positional,
#     *args,
#     keyword_only,
#     **kwargs
# ):
#     pass
# ```

# For example:

# ```python
# def test(a, b=10, *args, c=20, **kwargs):
#     print(a, b, args, c, kwargs)
# ```

# Don't worry about advanced combinations initially. Learn normal parameters, defaults, `*args`, and `**kwargs` first.

# ---

# # 17. Scope

# **Scope** means where a variable can be accessed.

# There are two important scopes:

# ```text
# Local
# Global
# ```

# ---

# ## 18. Local Variable

# A variable created inside a function is normally local.

# ```python
# def test():
#     x = 10
#     print(x)

# test()
# ```

# This works.

# But:

# ```python
# def test():
#     x = 10

# test()

# print(x)
# ```

# gives:

# ```text
# NameError
# ```

# because `x` belongs to the function's local scope.

# ---

# # 19. Global Variable

# A variable created outside a function is global.

# ```python
# x = 10

# def test():
#     print(x)

# test()
# ```

# Output:

# ```text
# 10
# ```

# The function can read the global variable.

# ---

# # 20. `global` Keyword

# If you want to modify a global variable from inside a function:

# ```python
# x = 10

# def change():
#     global x
#     x = 20

# change()

# print(x)
# ```

# Output:

# ```text
# 20
# ```

# Without `global`, assigning `x` inside the function creates a local variable.

# ---

# # 21. Nested Functions

# A function can be created inside another function.

# ```python
# def outer():

#     def inner():
#         print("Hello")

#     inner()

# outer()
# ```

# Output:

# ```text
# Hello
# ```

# ---

# # 22. Function Returning a Function

# Python functions are objects, so a function can return another function.

# ```python
# def outer():

#     def inner():
#         print("Hello")

#     return inner
# ```

# Then:

# ```python
# x = outer()

# x()
# ```

# Output:

# ```text
# Hello
# ```

# This leads to more advanced topics such as **closures and decorators**.

# ---

# # 23. Docstrings

# A docstring describes what a function does.

# ```python
# def add(a, b):
#     """Return the sum of two numbers."""
#     return a + b
# ```

# You can access it:

# ```python
# print(add.__doc__)
# ```

# Output:

# ```text
# Return the sum of two numbers.
# ```

# ---

# # 24. Type Hints

# You can specify expected types.

# ```python
# def add(a: int, b: int) -> int:
#     return a + b
# ```

# This means:

# ```text
# a → expected int
# b → expected int
# return → expected int
# ```

# Python generally **doesn't enforce these automatically**.

# ---

# # 25. Lambda Functions

# A lambda is a small anonymous function.

# Normal function:

# ```python
# def square(x):
#     return x * x
# ```

# Lambda:

# ```python
# square = lambda x: x * x
# ```

# Then:

# ```python
# print(square(5))
# ```

# Output:

# ```text
# 25
# ```

# Syntax:

# ```python
# lambda arguments: expression
# ```

# ---

# # 26. First-Class Functions

# Python treats functions as objects.

# You can store a function in a variable:

# ```python
# def greet():
#     print("Hello")

# x = greet

# x()
# ```

# Output:

# ```text
# Hello
# ```

# Notice:

# ```python
# x = greet
# ```

# not:

# ```python
# x = greet()
# ```

# The first stores the function itself.

# The second calls it.

# ---

# # 27. Passing a Function to Another Function

# ```python
# def greet():
#     print("Hello")

# def execute(function):
#     function()

# execute(greet)
# ```

# Output:

# ```text
# Hello
# ```

# This idea is important for:

# * `map()`
# * `filter()`
# * decorators
# * callbacks

# ---

# # Part 2 — Recursion

# ## 28. What is Recursion?

# **Recursion is when a function calls itself.**

# Example:

# ```python
# def countdown(n):

#     if n == 0:
#         return

#     print(n)

#     countdown(n - 1)
# ```

# Call:

# ```python
# countdown(5)
# ```

# Output:

# ```text
# 5
# 4
# 3
# 2
# 1
# ```

# Here:

# ```text
# countdown(5)
#     ↓
# countdown(4)
#     ↓
# countdown(3)
#     ↓
# countdown(2)
#     ↓
# countdown(1)
#     ↓
# countdown(0)
# ```

# ---

# # 29. Base Case

# Every useful recursive function needs a condition that **stops the recursion**.

# This is called the **base case**.

# ```python
# if n == 0:
#     return
# ```

# Without a base case:

# ```python
# def test():
#     test()
# ```

# The function keeps calling itself.

# Eventually Python gives:

# ```text
# RecursionError
# ```

# ---

# # 30. Recursive Case

# The part where the function calls itself is the **recursive case**.

# ```python
# countdown(n - 1)
# ```

# So recursion normally has:

# ```text
# 1. Base case
# 2. Recursive case
# ```

# ---

# # 31. Factorial Using Recursion

# Mathematically:

# ```text
# 5! = 5 × 4 × 3 × 2 × 1
# ```

# Recursive definition:

# ```text
# n! = n × (n-1)!
# ```

# Python:

# ```python
# def factorial(n):

#     if n == 0:
#         return 1

#     return n * factorial(n - 1)
# ```

# Call:

# ```python
# print(factorial(5))
# ```

# Output:

# ```text
# 120
# ```

# ---

# # 32. How Factorial Recursion Works

# For:

# ```python
# factorial(5)
# ```

# Python creates:

# ```text
# factorial(5)
# ↓
# 5 × factorial(4)
#        ↓
#        4 × factorial(3)
#               ↓
#               3 × factorial(2)
#                      ↓
#                      2 × factorial(1)
#                             ↓
#                             1 × factorial(0)
#                                    ↓
#                                    1
# ```

# Then the results return upward:

# ```text
# 1
# 1 × 1 = 1
# 2 × 1 = 2
# 3 × 2 = 6
# 4 × 6 = 24
# 5 × 24 = 120
# ```

# ---

# # 33. Recursive Sum

# Calculate:

# ```text
# 1 + 2 + 3 + 4 + 5
# ```

# ```python
# def total(n):

#     if n == 0:
#         return 0

#     return n + total(n - 1)
# ```

# ```python
# print(total(5))
# ```

# Output:

# ```text
# 15
# ```

# ---

# # 34. Fibonacci Recursion

# Fibonacci sequence:

# ```text
# 0 1 1 2 3 5 8 13 ...
# ```

# A recursive version:

# ```python
# def fibonacci(n):

#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)
# ```

# Example:

# ```python
# print(fibonacci(6))
# ```

# Output:

# ```text
# 8
# ```

# This simple recursive version becomes slow for larger `n` because it repeats many calculations.

# ---

# # 35. Recursion vs Loop

# The factorial can be written with a loop:

# ```python
# def factorial(n):

#     result = 1

#     for i in range(1, n + 1):
#         result *= i

#     return result
# ```

# Or recursion:

# ```python
# def factorial(n):

#     if n == 0:
#         return 1

#     return n * factorial(n - 1)
# ```

# ### Think:

# ```text
# Loop
# → repeat using iteration

# Recursion
# → repeat using function calls
# ```

# ---

# # 36. Recursion Call Stack

# When a function calls itself, Python stores each function call in a **call stack**.

# For:

# ```python
# factorial(3)
# ```

# you can imagine:

# ```text
# ┌──────────────┐
# │ factorial(1) │
# ├──────────────┤
# │ factorial(2) │
# ├──────────────┤
# │ factorial(3) │
# └──────────────┘
# ```

# The last call is completed first.

# This is called **LIFO**:

# > Last In, First Out.

# ---

# # 37. Recursion Depth

# Python limits how deeply recursion can normally go.

# You can see the recursion limit:

# ```python
# import sys

# print(sys.getrecursionlimit())
# ```

# You should generally **not** solve ordinary repetitive tasks with recursion just because you can. A loop is often simpler and more memory-efficient.

# ---

# # 38. Recursion with Strings

# Example: reverse a string.

# ```python
# def reverse(text):

#     if text == "":
#         return ""

#     return reverse(text[1:]) + text[0]
# ```

# ```python
# print(reverse("hello"))
# ```

# Output:

# ```text
# olleh
# ```

# ---

# # 39. Recursion with Lists

# Calculate the sum of a list recursively:

# ```python
# def list_sum(numbers):

#     if len(numbers) == 0:
#         return 0

#     return numbers[0] + list_sum(numbers[1:])
# ```

# ```python
# print(list_sum([1, 2, 3, 4]))
# ```

# Output:

# ```text
# 10
# ```

# ---

# # 40. Important Function Concepts — Revision

# ```text
# Function
# ├── def
# ├── calling
# ├── parameters
# ├── arguments
# ├── return
# ├── default parameters
# ├── positional arguments
# ├── keyword arguments
# ├── *args
# ├── **kwargs
# ├── scope
# │   ├── local
# │   └── global
# ├── global keyword
# ├── nested functions
# ├── docstrings
# ├── type hints
# ├── lambda
# └── first-class functions
# ```

# # 41. Important Recursion Concepts

# ```text
# Recursion
# ├── function calls itself
# ├── base case
# ├── recursive case
# ├── call stack
# ├── recursion depth
# ├── RecursionError
# ├── factorial
# ├── Fibonacci
# ├── recursive sum
# └── recursion vs iteration
# ```

# ## The most important pattern

# When you see a recursion question, first find these two things:

# ```python
# def function(n):

#     # 1. BASE CASE
#     if ...:
#         return ...

#     # 2. RECURSIVE CASE
#     return ... function(...)
# ```

# For example:

# ```python
# def factorial(n):

#     # Base case
#     if n == 0:
#         return 1

#     # Recursive case
#     return n * factorial(n - 1)
# ```

# **Memory trick:**

# > **Recursion = Base Case + Smaller Problem + Self-Call**.
