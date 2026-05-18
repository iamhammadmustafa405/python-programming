# String Functions.
# str= "hammad Mustafa"
# # str = str.capitalize()
# # print(str)
# # print(str.endswith("afa"))

# str= "I am Studying Python from apnacollege."
# print(str.replace("Python","Java"))
# print(str.find("Python"))
# print(str.count("m"))


# Below is a **simple and clear explanation of Python string methods**, grouped and explained in easy words.

# ---

# ## What are String Methods?

# String methods are **built-in functions** that work on text (`str`).
# They **do not change the original string** (strings are immutable).
# They always **return a new string or a result**.

# Example:

# ```python
# s = "hello"
# print(s.upper())   # HELLO
# print(s)           # hello (original unchanged)
# ```

# ---

# ## 1. Case Conversion Methods

# Used to change letter case.

# * `upper()` → makes all letters CAPITAL
# * `lower()` → makes all letters small
# * `capitalize()` → first letter capital
# * `title()` → first letter of every word capital
# * `swapcase()` → small → capital, capital → small
# * `casefold()` → stronger lowercase (used for comparisons)

# ```python
# "hello world".title()   # Hello World
# ```

# ---

# ## 2. Removing Spaces (Trimming)

# Used to remove unwanted spaces.

# * `strip()` → removes spaces from both sides
# * `lstrip()` → removes left spaces
# * `rstrip()` → removes right spaces

# ```python
# "  hi  ".strip()   # "hi"
# ```

# ---

# ## 3. Searching in Strings

# Used to find text.

# * `find()` → position of text (−1 if not found)
# * `index()` → same as find but gives error if not found
# * `count()` → how many times text appears

# ```python
# "banana".find("na")   # 2
# "banana".count("a")  # 3
# ```

# ---

# ## 4. Checking Methods (True / False)

# Used to **check string properties**.

# * `isalpha()` → only letters
# * `isdigit()` → only numbers
# * `isalnum()` → letters + numbers
# * `isspace()` → only spaces
# * `islower()` / `isupper()` → case check
# * `startswith()` / `endswith()` → checks start/end

# ```python
# "123".isdigit()        # True
# "Hello".isupper()     # False
# ```

# ---

# ## 5. Replace & Modify

# Used to change text.

# * `replace(old, new)` → replaces text
# * `translate()` → advanced character replacement

# ```python
# "I like tea".replace("tea", "coffee")
# ```

# ---

# ## 6. Split & Join

# Used to break or connect strings.

# * `split()` → converts string into list
# * `join()` → joins list into string

# ```python
# "one two three".split()
# ",".join(["a", "b", "c"])
# ```

# ---

# ## 7. Alignment & Padding

# Used in formatting output.

# * `center()` → center text
# * `ljust()` → left align
# * `rjust()` → right align
# * `zfill()` → fills zeros in front

# ```python
# "5".zfill(3)   # 005
# ```

# ---

# ## 8. Prefix & Suffix Removal

# Used to remove known words.

# * `removeprefix()`
# * `removesuffix()`

# ```python
# "unhappy".removeprefix("un")   # happy
# ```

# ---

# ## 9. Formatting Strings

# Used to insert values.

# * `format()`
# * `format_map()`

# ```python
# "My name is {}".format("Ali")
# ```

# ---

# ## 10. Encoding

# Used to convert string to bytes.

# * `encode()`

# ```python
# "hello".encode()
# ```

# ---

# ## Key Point to Remember

# ✔ Strings are **immutable**
# ✔ Methods return **new values**
# ✔ Original string stays same

# ---

# If you want:

# * **Very short one-line explanations**
# * **Practice questions**
# * **Common mistakes**
# * **Methods for beginners only**

# tell me exactly what you want next.
