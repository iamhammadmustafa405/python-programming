# Below are the **core properties of Python strings**, explained clearly and simply.

# ---

# ## 1. Strings are Immutable

# Once a string is created, **it cannot be changed**.

# ```python
# s = "hello"
# # s[0] = "H"   ❌ Error
# s = "Hello"    # ✔ New string
# ```

# ---

# ## 2. Strings are Ordered

# Each character has a **fixed position (index)**.

# ```python
# s = "Python"
# print(s[0])   # P
# print(s[5])   # n
# ```

# ---

# ## 3. Strings Support Indexing

# You can access characters using **index numbers**.

# * Positive index → from left (`0,1,2...`)
# * Negative index → from right (`-1,-2...`)

# ```python
# s = "Python"
# print(s[-1])  # n
# ```

# ---

# ## 4. Strings Support Slicing

# You can extract a **part of a string**.

# ```python
# s = "Programming"
# print(s[0:6])   # Progra
# print(s[::2])   # Pormig
# ```

# ---

# ## 5. Strings Can Be Iterated

# You can loop through each character.

# ```python
# for ch in "Hi":
#     print(ch)
# ```

# ---

# ## 6. Strings Support Concatenation

# Strings can be **joined using +**.

# ```python
# a = "Hello"
# b = "World"
# print(a + " " + b)
# ```

# ---

# ## 7. Strings Support Repetition

# Strings can be repeated using `*`.

# ```python
# print("Ha" * 3)   # HaHaHa
# ```

# ---

# ## 8. Strings Have Length

# You can find length using `len()`.

# ```python
# len("Python")   # 6
# ```

# ---

# ## 9. Strings Support Membership

# You can check if a character or word exists.

# ```python
# "a" in "apple"       # True
# "x" not in "apple"   # True
# ```

# ---

# ## 10. Strings Can Be Compared

# Strings can be compared using comparison operators.

# ```python
# "apple" == "apple"   # True
# "apple" < "banana"   # True (dictionary order)
# ```

# ---

# ## 11. Strings Can Be Multi-line

# Strings can span **multiple lines**.

# ```python
# s = """Hello
# World"""
# ```

# ---

# ## 12. Strings Support Escape Characters

# Special characters are supported.

# ```python
# print("Hello\nWorld")
# print("Tab\tSpace")
# ```

# ---

# ## 13. Strings Are Unicode

# Python strings support **Unicode characters**.

# ```python
# print("پاکستان")
# print("😊")
# ```

# ---

# ## 14. Strings Are Objects

# Strings belong to class `str` and have many methods.

# ```python
# type("hello")   # <class 'str'>
# ```

# ---

# ## 15. Strings Can Be Created in Multiple Ways

# ```python
# s1 = "text"
# s2 = 'text'
# s3 = """text"""
# ```

# ---

# ## Summary (One-Line)

# **Python strings are immutable, ordered, iterable sequences of Unicode characters that support indexing, slicing, and many built-in methods.**

