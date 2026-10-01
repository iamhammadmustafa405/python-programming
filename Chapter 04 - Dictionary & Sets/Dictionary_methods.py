# # Python Dictionary — All Methods

# A **dictionary (`dict`)** stores data as **key-value pairs**.

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 85
# }
# ```

# Here:

# ```text
# "name"  → key
# "Hammad" → value
# ```

# Python dictionaries have **11 main built-in methods**.

# ---

# ## 1. `clear()`

# Removes **all items** from the dictionary.

# ```python
# student = {"name": "Hammad", "age": 19}

# student.clear()

# print(student)
# ```

# Output:

# ```text
# {}
# ```

# ---

# ## 2. `copy()`

# Creates a **shallow copy** of the dictionary.

# ```python
# student = {"name": "Hammad", "age": 19}

# new_student = student.copy()

# print(new_student)
# ```

# Output:

# ```text
# {'name': 'Hammad', 'age': 19}
# ```

# It is similar to:

# ```python
# new_student = copy.copy(student)
# ```

# ---

# ## 3. `fromkeys()`

# Creates a new dictionary using given keys and one common value.

# ```python
# keys = ["name", "age", "marks"]

# student = dict.fromkeys(keys)

# print(student)
# ```

# Output:

# ```text
# {'name': None, 'age': None, 'marks': None}
# ```

# You can provide a value:

# ```python
# student = dict.fromkeys(keys, 0)

# print(student)
# ```

# Output:

# ```text
# {'name': 0, 'age': 0, 'marks': 0}
# ```

# ---

# ## 4. `get()`

# Gets the value of a key.

# ```python
# student = {"name": "Hammad", "age": 19}

# print(student.get("name"))
# ```

# Output:

# ```text
# Hammad
# ```

# ### Why use `get()`?

# If the key doesn't exist:

# ```python
# print(student.get("height"))
# ```

# Output:

# ```text
# None
# ```

# But:

# ```python
# print(student["height"])
# ```

# gives:

# ```text
# KeyError
# ```

# You can also give a default value:

# ```python
# print(student.get("height", 0))
# ```

# Output:

# ```text
# 0
# ```

# ---

# # 5. `items()`

# Returns **key-value pairs**.

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19
# }

# print(student.items())
# ```

# Output:

# ```text
# dict_items([('name', 'Hammad'), ('age', 19)])
# ```

# Very commonly used with loops:

# ```python
# for key, value in student.items():
#     print(key, value)
# ```

# Output:

# ```text
# name Hammad
# age 19
# ```

# ---

# # 6. `keys()`

# Returns all the **keys**.

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 85
# }

# print(student.keys())
# ```

# Output:

# ```text
# dict_keys(['name', 'age', 'marks'])
# ```

# Example:

# ```python
# for key in student.keys():
#     print(key)
# ```

# ---

# # 7. `pop()`

# Removes a specified key and **returns its value**.

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19
# }

# x = student.pop("age")

# print(x)
# print(student)
# ```

# Output:

# ```text
# 19
# {'name': 'Hammad'}
# ```

# You can provide a default:

# ```python
# student.pop("height", 0)
# ```

# If `"height"` doesn't exist, it returns `0` instead of giving an error.

# ---

# # 8. `popitem()`

# Removes and returns the **last key-value pair**.

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 85
# }

# x = student.popitem()

# print(x)
# print(student)
# ```

# Output:

# ```text
# ('marks', 85)
# {'name': 'Hammad', 'age': 19}
# ```

# Think:

# ```text
# pop()      → remove a specific key
# popitem()  → remove the last item
# ```

# ---

# # 9. `setdefault()`

# Returns the value of a key.

# If the key **doesn't exist**, it creates the key with a default value.

# ```python
# student = {"name": "Hammad"}

# x = student.setdefault("age", 19)

# print(x)
# print(student)
# ```

# Output:

# ```text
# 19
# {'name': 'Hammad', 'age': 19}
# ```

# If the key already exists:

# ```python
# student = {"name": "Hammad", "age": 19}

# student.setdefault("age", 25)

# print(student)
# ```

# Output:

# ```text
# {'name': 'Hammad', 'age': 19}
# ```

# It does **not overwrite** the existing value.

# ---

# # 10. `update()`

# Adds new key-value pairs or **updates existing ones**.

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19
# }

# student.update({"marks": 85})

# print(student)
# ```

# Output:

# ```text
# {'name': 'Hammad', 'age': 19, 'marks': 85}
# ```

# If the key already exists:

# ```python
# student.update({"age": 20})
# ```

# Now:

# ```text
# {'name': 'Hammad', 'age': 20, 'marks': 85}
# ```

# ---

# # 11. `values()`

# Returns all the **values**.

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 85
# }

# print(student.values())
# ```

# Output:

# ```text
# dict_values(['Hammad', 19, 85])
# ```

# Example:

# ```python
# for value in student.values():
#     print(value)
# ```

# ---

# # Quick Revision Table

# | Method         | Purpose                          |
# | -------------- | -------------------------------- |
# | `clear()`      | Remove everything                |
# | `copy()`       | Make a shallow copy              |
# | `fromkeys()`   | Create dictionary from keys      |
# | `get()`        | Get value safely                 |
# | `items()`      | Get key-value pairs              |
# | `keys()`       | Get keys                         |
# | `pop()`        | Remove specified key             |
# | `popitem()`    | Remove last item                 |
# | `setdefault()` | Get value; create key if missing |
# | `update()`     | Add/update items                 |
# | `values()`     | Get values                       |

# ## ⭐ The 11 methods

# ```text
# clear()
# copy()
# fromkeys()
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()
# ```

# ### One important distinction

# These are **dictionary methods**:

# ```python
# student.keys()
# student.values()
# student.items()
# ```

# But these are **built-in functions**, not dictionary methods:

# ```python
# len(student)
# type(student)
# str(student)
# ```

# And you can access dictionary data directly with:

# ```python
# student["name"]
# ```

# which is **dictionary indexing**, not a method.
