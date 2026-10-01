# # Serialization & Deserialization in Python

# ## 1. What is Serialization?

# **Serialization = Python object → data that can be stored or transmitted.**

# Think of it like **packing your Python object into a box**.

# Example:

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 90
# }
# ```

# We can serialize this dictionary into JSON:

# ```text
# Python object
#      ↓
# Serialization
#      ↓
# JSON data
# ```

# ---

# # 2. What is Deserialization?

# **Deserialization = stored/transmitted data → Python object.**

# It is the opposite process.

# ```text
# JSON data
#      ↓
# Deserialization
#      ↓
# Python object
# ```

# ### Easy memory trick

# > **Serialize = Pack** 📦
# > **Deserialize = Unpack**

# ---

# # 3. Why do we need Serialization?

# Suppose you have:

# ```python
# student = {
#     "name": "Hammad",
#     "age": 19
# }
# ```

# Python can use this object while the program is running.

# But you may want to:

# * save it to a file
# * send it through an API
# * store it in a database
# * send it over a network
# * transfer it to another program

# Serialization converts the object into a suitable format.

# ---

# # 4. JSON Serialization

# The most common format is **JSON**.

# Python provides the built-in `json` module.

# ```python
# import json
# ```

# ---

# ## 5. `json.dumps()` — Serialization

# `dumps()` means:

# > **Convert Python object → JSON string**

# ```python
# import json

# student = {
#     "name": "Hammad",
#     "age": 19
# }

# data = json.dumps(student)

# print(data)
# print(type(data))
# ```

# Output:

# ```text
# {"name": "Hammad", "age": 19}
# <class 'str'>
# ```

# Notice:

# ```text
# Python dictionary
#        ↓
#    json.dumps()
#        ↓
# JSON string
# ```

# ---

# # 6. `json.loads()` — Deserialization

# `loads()` means:

# > **Convert JSON string → Python object**

# ```python
# import json

# data = '{"name": "Hammad", "age": 19}'

# student = json.loads(data)

# print(student)
# print(type(student))
# ```

# Output:

# ```text
# {'name': 'Hammad', 'age': 19}
# <class 'dict'>
# ```

# ---

# # 7. `dump()` vs `dumps()`

# This is very important.

# ### `dumps()`

# Used when you want a **JSON string**.

# ```python
# json.dumps(data)
# ```

# ### `dump()`

# Used when you want to **write JSON directly into a file**.

# ```python
# json.dump(data, file)
# ```

# Think:

# ```text
# dump   → file
# dumps  → string
# ```

# ---

# # 8. `load()` vs `loads()`

# Same idea.

# ### `loads()`

# JSON string → Python object

# ```python
# json.loads(data)
# ```

# ### `load()`

# JSON file → Python object

# ```python
# json.load(file)
# ```

# Memory trick:

# ```text
# load   → file
# loads  → string
# ```

# ---

# # 9. Complete JSON File Example

# ### Serialization

# ```python
# import json

# student = {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 90
# }

# with open("student.json", "w") as file:
#     json.dump(student, file)
# ```

# This creates:

# ```text
# student.json
# ```

# Containing:

# ```json
# {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 90
# }
# ```

# ---

# ### Deserialization

# ```python
# import json

# with open("student.json", "r") as file:
#     student = json.load(file)

# print(student)
# ```

# Output:

# ```python
# {'name': 'Hammad', 'age': 19, 'marks': 90}
# ```

# ---

# # 10. Python → JSON Conversion

# JSON has its own data types.

# | Python  | JSON    |
# | ------- | ------- |
# | `dict`  | object  |
# | `list`  | array   |
# | `tuple` | array   |
# | `str`   | string  |
# | `int`   | number  |
# | `float` | number  |
# | `True`  | `true`  |
# | `False` | `false` |
# | `None`  | `null`  |

# Example:

# ```python
# data = {
#     "name": "Hammad",
#     "age": 19,
#     "student": True,
#     "skills": ["Python", "C++"],
#     "address": None
# }
# ```

# Serialization:

# ```python
# json.dumps(data)
# ```

# Result:

# ```json
# {
#     "name": "Hammad",
#     "age": 19,
#     "student": true,
#     "skills": ["Python", "C++"],
#     "address": null
# }
# ```

# Notice:

# ```python
# True
# ```

# becomes:

# ```json
# true
# ```

# and:

# ```python
# None
# ```

# becomes:

# ```json
# null
# ```

# ---

# # 11. JSON Serialization Example

# ```python
# import json

# data = {
#     "name": "Ali",
#     "age": 20,
#     "skills": ["Python", "SQL"]
# }

# json_data = json.dumps(data)

# print(json_data)
# ```

# ### Flow

# ```text
# dict
#  ↓
# json.dumps()
#  ↓
# JSON string
# ```

# ---

# # 12. JSON Deserialization Example

# ```python
# import json

# json_data = '{"name": "Ali", "age": 20}'

# data = json.loads(json_data)

# print(data["name"])
# ```

# Output:

# ```text
# Ali
# ```

# ### Flow

# ```text
# JSON string
#  ↓
# json.loads()
#  ↓
# dict
# ```

# ---

# # 13. Pretty JSON

# You can make JSON easier to read using `indent`.

# ```python
# import json

# student = {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 90
# }

# print(json.dumps(student, indent=4))
# ```

# Output:

# ```json
# {
#     "name": "Hammad",
#     "age": 19,
#     "marks": 90
# }
# ```

# ---

# # 14. Sorting JSON Keys

# ```python
# print(json.dumps(student, indent=4, sort_keys=True))
# ```

# This sorts dictionary keys alphabetically.

# ---

# # 15. Serialization with `pickle`

# Python also has another serialization system:

# ```python
# import pickle
# ```

# `pickle` can serialize many Python-specific objects.

# Example:

# ```python
# import pickle

# student = {
#     "name": "Hammad",
#     "age": 19
# }

# data = pickle.dumps(student)

# print(data)
# ```

# The result is **binary data**, not normal readable text.

# ---

# # 16. Pickle Deserialization

# ```python
# student = pickle.loads(data)

# print(student)
# ```

# Output:

# ```python
# {'name': 'Hammad', 'age': 19}
# ```

# ---

# # 17. Pickle with Files

# ### Serialize

# ```python
# import pickle

# student = {
#     "name": "Hammad",
#     "age": 19
# }

# with open("student.pkl", "wb") as file:
#     pickle.dump(student, file)
# ```

# Notice:

# ```python
# "wb"
# ```

# means:

# > write binary

# ---

# ### Deserialize

# ```python
# with open("student.pkl", "rb") as file:
#     student = pickle.load(file)

# print(student)
# ```

# `rb` means:

# > read binary

# ---

# # 18. JSON vs Pickle

# | JSON                      | Pickle                       |
# | ------------------------- | ---------------------------- |
# | Human-readable            | Binary                       |
# | Language-independent      | Mainly Python                |
# | Good for APIs             | Good for Python objects      |
# | Safer for exchanging data | Never load untrusted pickle  |
# | Limited Python objects    | Supports many Python objects |

# ### Simple rule

# Use:

# **JSON** → APIs, web, data exchange

# **Pickle** → Python-specific object storage

# ---

# # 19. Important Pickle Security Rule

# **Never unpickle data from an untrusted source.**

# For example, don't blindly do:

# ```python
# pickle.load(untrusted_file)
# ```

# Pickle can execute malicious code during deserialization.

# JSON does not have this same pickle-style execution risk.

# ---

# # 20. Custom Object Serialization

# Suppose we have:

# ```python
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# ```

# Create object:

# ```python
# student = Student("Hammad", 19)
# ```

# `json.dumps()` cannot directly serialize this object:

# ```python
# json.dumps(student)
# ```

# This produces a `TypeError`.

# Why?

# Because JSON doesn't automatically know how to convert a custom `Student` object.

# ---

# # 21. Converting Custom Object to Dictionary

# We can manually convert it:

# ```python
# data = {
#     "name": student.name,
#     "age": student.age
# }

# json_data = json.dumps(data)

# print(json_data)
# ```

# Output:

# ```json
# {"name": "Hammad", "age": 19}
# ```

# ---

# # 22. Custom Encoder

# For more advanced situations, Python allows a custom JSON encoder.

# ```python
# import json

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class StudentEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Student):
#             return {
#                 "name": obj.name,
#                 "age": obj.age
#             }

#         return super().default(obj)


# student = Student("Hammad", 19)

# data = json.dumps(student, cls=StudentEncoder)

# print(data)
# ```

# Output:

# ```json
# {"name": "Hammad", "age": 19}
# ```

# ---

# # 23. Deserializing Custom Objects

# After getting JSON:

# ```json
# {"name": "Hammad", "age": 19}
# ```

# we can create the object again:

# ```python
# data = json.loads(json_data)

# student = Student(
#     data["name"],
#     data["age"]
# )

# print(student.name)
# print(student.age)
# ```

# Output:

# ```text
# Hammad
# 19
# ```

# ---

# # 24. Serialization in APIs

# Serialization is extremely important in web development.

# Suppose Python has:

# ```python
# user = {
#     "name": "Hammad",
#     "age": 19
# }
# ```

# An API may serialize it:

# ```text
# Python dictionary
#        ↓
#      JSON
#        ↓
#      HTTP
#        ↓
#     Internet
# ```

# The other application receives JSON and deserializes it:

# ```text
# JSON
#  ↓
# Python dictionary
# ```

# This is one reason JSON is so common in APIs.

# ---

# # 25. Serialization vs Deserialization

# | Concept                | Meaning                                | Common function  |
# | ---------------------- | -------------------------------------- | ---------------- |
# | Serialization          | Object → storable/transmittable format | `json.dumps()`   |
# | Deserialization        | Format → Python object                 | `json.loads()`   |
# | File serialization     | Object → JSON file                     | `json.dump()`    |
# | File deserialization   | JSON file → object                     | `json.load()`    |
# | Pickle serialization   | Object → binary                        | `pickle.dumps()` |
# | Pickle deserialization | Binary → object                        | `pickle.loads()` |

# ---

# # 26. The 4 JSON Functions

# Remember these four:

# ```text
#              JSON
#           /         \
#       String       File
#         |            |
#       dumps         dump
#         ↑            ↑
#    Python object → JSON
# ```

# And reverse:

# ```text
#              JSON
#           /         \
#       String       File
#         |            |
#       loads         load
#         ↓            ↓
#           Python object
# ```

# ### Easy memory trick

# > **S = String**
# > **No S = File**

# ```python
# dumps  → string
# dump   → file

# loads  → string
# load   → file
# ```

# ---

# ## Explanation

# Serialization is simply **turning an object into a form that can be saved or sent**.
# Deserialization is **turning that saved/sent form back into an object**.
# For beginners, focus first on **JSON + `dump/dumps/load/loads`**.
# Later, learn `pickle` for Python-specific objects.
# A very common mistake is confusing `dump` with `dumps` and `load` with `loads`.

# ### Most important example

# ```python
# import json

# student = {"name": "Hammad", "age": 19}

# # Serialization
# text = json.dumps(student)

# # Deserialization
# student_again = json.loads(text)

# print(student_again)
# ```

# ```text
# Python dict
#     ↓
# json.dumps()
#     ↓
# JSON string
#     ↓
# json.loads()
#     ↓
# Python dict
# ```

# This is the core idea of serialization and deserialization.
