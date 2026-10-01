# # Python Modules & Packages — Full Guide

# ## 1. What is a Module?

# A **module** is simply a Python file (`.py`) containing code that you can reuse.

# Example:

# ```text
# math_tools.py
# ```

# Inside:

# ```python
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b
# ```

# Now another file can use it.

# ```python
# import math_tools

# print(math_tools.add(5, 3))
# print(math_tools.subtract(5, 3))
# ```

# Output:

# ```text
# 8
# 2
# ```

# ### Explanation

# Think of a module as a **toolbox**.

# Instead of writing the same functions again and again, you put them in one `.py` file and import them whenever needed.

# ---

# # 2. Why Use Modules?

# Modules help you:

# * Reuse code
# * Organize large programs
# * Make code easier to maintain
# * Avoid repeating code
# * Keep related functions/classes together

# Instead of:

# ```text
# main.py
# # 5000 lines of code
# ```

# you can have:

# ```text
# main.py
# calculator.py
# database.py
# users.py
# ```

# ---

# # 3. Different Types of Modules

# Python modules generally come from three places:

# ### 1. Built-in/standard library modules

# Already included with Python:

# ```python
# import math
# import os
# import random
# import json
# import datetime
# ```

# ### 2. Your own modules

# You create them:

# ```text
# calculator.py
# ```

# ### 3. Third-party modules

# Installed separately:

# ```bash
# pip install requests
# ```

# Then:

# ```python
# import requests
# ```

# ---

# # 4. `import`

# The simplest way:

# ```python
# import math

# print(math.sqrt(25))
# ```

# Output:

# ```text
# 5.0
# ```

# General form:

# ```python
# import module_name
# ```

# Access something using:

# ```python
# module_name.object
# ```

# Example:

# ```python
# import random

# print(random.randint(1, 10))
# ```

# ---

# # 5. Import Multiple Modules

# ```python
# import math
# import random
# import os
# ```

# You can also:

# ```python
# import math, random, os
# ```

# But separate imports are usually easier to read.

# ---

# # 6. `from ... import`

# Instead of importing the entire module:

# ```python
# from math import sqrt

# print(sqrt(25))
# ```

# You don't need:

# ```python
# math.sqrt(25)
# ```

# You can import multiple things:

# ```python
# from math import sqrt, pi

# print(sqrt(25))
# print(pi)
# ```

# ---

# # 7. Import Everything Using `*`

# ```python
# from math import *
# ```

# Now:

# ```python
# print(sqrt(25))
# print(pi)
# ```

# ### Why is this usually discouraged?

# Because you may not know where a name came from.

# For example:

# ```python
# from math import *
# from another_module import *
# ```

# Both modules could contain a function called:

# ```python
# calculate()
# ```

# One can overwrite the other.

# Prefer:

# ```python
# import math
# ```

# or:

# ```python
# from math import sqrt
# ```

# ---

# # 8. Import With an Alias

# You can give a module a shorter name.

# ```python
# import math as m

# print(m.sqrt(25))
# ```

# Another common example:

# ```python
# import numpy as np
# ```

# Then:

# ```python
# np.array([1, 2, 3])
# ```

# The alias only changes how **you refer to it**.

# ---

# # 9. Alias With `from`

# ```python
# from math import sqrt as s

# print(s(25))
# ```

# ---

# # 10. Your Own Module

# Suppose your folder contains:

# ```text
# project/
# │
# ├── main.py
# └── calculator.py
# ```

# ### calculator.py

# ```python
# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b
# ```

# ### main.py

# ```python
# import calculator

# print(calculator.add(5, 3))
# print(calculator.multiply(5, 3))
# ```

# Output:

# ```text
# 8
# 15
# ```

# ---

# # 11. Importing Specific Functions From Your Module

# ```python
# from calculator import add

# print(add(5, 3))
# ```

# Multiple:

# ```python
# from calculator import add, multiply
# ```

# ---

# # 12. Variables Inside Modules

# Modules can contain variables too.

# ### config.py

# ```python
# name = "Hammad"
# age = 19
# ```

# ### main.py

# ```python
# import config

# print(config.name)
# print(config.age)
# ```

# ---

# # 13. Classes Inside Modules

# ### student.py

# ```python
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(self.name)
# ```

# ### main.py

# ```python
# from student import Student

# s1 = Student("Hammad")
# s1.show()
# ```

# ---

# # 14. Functions + Classes + Variables

# A module can contain all of them:

# ```python
# PI = 3.14159

# def square(x):
#     return x * x

# class Calculator:
#     def add(self, a, b):
#         return a + b
# ```

# ---

# # 15. What Happens When You Import a Module?

# Suppose:

# ```python
# # test.py

# print("Hello")
# ```

# Then:

# ```python
# import test
# ```

# Python executes the module.

# Output:

# ```text
# Hello
# ```

# This is important.

# ---

# # 16. `if __name__ == "__main__"`

# This is one of the **most important concepts in modules**.

# Example:

# ```python
# # calculator.py

# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print(add(5, 3))
# ```

# If you directly run:

# ```bash
# python calculator.py
# ```

# Python runs:

# ```python
# print(add(5, 3))
# ```

# But if another file does:

# ```python
# import calculator
# ```

# the code inside:

# ```python
# if __name__ == "__main__":
# ```

# doesn't run.

# ### Why?

# When a file is directly executed:

# ```python
# __name__ == "__main__"
# ```

# When imported:

# ```python
# __name__ == "calculator"
# ```

# This allows one file to work both as a reusable module and as a standalone program.

# ---

# # 17. What is a Package?

# A **package** is a folder containing related Python modules.

# Example:

# ```text
# myproject/
# │
# ├── main.py
# │
# └── tools/
#     ├── __init__.py
#     ├── calculator.py
#     └── converter.py
# ```

# Here:

# ```text
# tools
# ```

# is a package.

# And:

# ```text
# calculator.py
# converter.py
# ```

# are modules.

# ### Easy way to remember

# ```text
# Module  = file
# Package = folder of modules
# ```

# ---

# # 18. `__init__.py`

# Traditionally, a package contains:

# ```text
# __init__.py
# ```

# Example:

# ```text
# tools/
# ├── __init__.py
# ├── calculator.py
# └── converter.py
# ```

# It tells Python that the directory is intended to be a package.

# Modern Python also supports **namespace packages**, where `__init__.py` is not required in certain situations. However, for learning and ordinary project organization, you will often see it included.

# ---

# # 19. Importing From a Package

# Structure:

# ```text
# project/
# │
# ├── main.py
# └── tools/
#     ├── __init__.py
#     └── calculator.py
# ```

# `calculator.py`:

# ```python
# def add(a, b):
#     return a + b
# ```

# `main.py`:

# ```python
# from tools import calculator

# print(calculator.add(5, 3))
# ```

# ---

# # 20. Import Directly From a Package Module

# ```python
# from tools.calculator import add

# print(add(5, 3))
# ```

# Structure:

# ```text
# tools.calculator
# ```

# means:

# ```text
# package.module
# ```

# ---

# # 21. Multiple Modules in a Package

# ```text
# tools/
# ├── __init__.py
# ├── calculator.py
# ├── converter.py
# └── validator.py
# ```

# You can use:

# ```python
# from tools.calculator import add
# from tools.converter import km_to_miles
# from tools.validator import validate_email
# ```

# ---

# # 22. Subpackages

# Packages can contain other packages.

# ```text
# project/
# │
# ├── main.py
# └── app/
#     ├── __init__.py
#     │
#     ├── database/
#     │   ├── __init__.py
#     │   └── connection.py
#     │
#     └── users/
#         ├── __init__.py
#         └── user.py
# ```

# Now:

# ```python
# from app.database.connection import connect
# ```

# The structure is:

# ```text
# app
#  ↓
# database
#  ↓
# connection
#  ↓
# connect
# ```

# ---

# # 23. Absolute Imports

# An absolute import starts from the package's top-level location.

# Example:

# ```python
# from app.database.connection import connect
# ```

# This is usually easier to understand.

# ---

# # 24. Relative Imports

# Inside a package, you can use:

# ```python
# from .calculator import add
# ```

# `.` means:

# > Current package.

# Example:

# ```text
# tools/
# ├── __init__.py
# ├── calculator.py
# └── converter.py
# ```

# Inside `converter.py`:

# ```python
# from .calculator import add
# ```

# ---

# # 25. `..` in Relative Imports

# Two dots mean:

# > Go to the parent package.

# Example:

# ```python
# from ..database.connection import connect
# ```

# `.` → current package

# `..` → parent package

# ---

# # 26. Standard Library Packages

# Python comes with many useful modules/packages.

# Examples:

# ```python
# import os
# import sys
# import math
# import random
# import json
# import csv
# import datetime
# import pathlib
# import statistics
# ```

# You don't need to install these separately.

# ---

# # 27. Third-Party Packages

# These are created by other developers.

# Examples:

# ```text
# NumPy
# Pandas
# Requests
# Matplotlib
# FastAPI
# Django
# ```

# Usually installed with:

# ```bash
# pip install package_name
# ```

# Example:

# ```bash
# pip install requests
# ```

# Then:

# ```python
# import requests
# ```

# ---

# # 28. What is `pip`?

# `pip` is Python's package installer.

# Example:

# ```bash
# pip install requests
# ```

# Remove:

# ```bash
# pip uninstall requests
# ```

# Upgrade:

# ```bash
# pip install --upgrade requests
# ```

# See installed packages:

# ```bash
# pip list
# ```

# Show package information:

# ```bash
# pip show requests
# ```

# ---

# # 29. `requirements.txt`

# For a project, you can save dependencies:

# ```text
# requests==2.32.5
# numpy==2.3.3
# pandas==2.3.3
# ```

# Install them:

# ```bash
# pip install -r requirements.txt
# ```

# Create one from your environment:

# ```bash
# pip freeze > requirements.txt
# ```

# ---

# # 30. Virtual Environments

# Packages should usually be installed inside a project's virtual environment.

# Create:

# ```bash
# python -m venv .venv
# ```

# Activate on Windows:

# ```bash
# .venv\Scripts\activate
# ```

# Then:

# ```bash
# python -m pip install requests
# ```

# This keeps one project's packages separate from another project's packages.

# ---

# # 31. `python -m pip`

# Instead of:

# ```bash
# pip install pandas
# ```

# you can use:

# ```bash
# python -m pip install pandas
# ```

# This is often safer because it clearly uses the `pip` associated with that Python interpreter.

# ---

# # 32. Module Search Path

# When you write:

# ```python
# import something
# ```

# Python searches certain locations to find `something`.

# You can see them with:

# ```python
# import sys

# print(sys.path)
# ```

# `sys.path` contains directories Python searches for modules.

# ---

# # 33. `__pycache__`

# After importing a module, Python may create:

# ```text
# __pycache__/
# ```

# Inside you may see:

# ```text
# calculator.cpython-314.pyc
# ```

# This contains compiled bytecode used by Python to speed up loading.

# You normally don't need to edit it.

# ---

# # 34. Module Naming Rules

# A module should normally have a simple name:

# ```text
# calculator.py
# database.py
# student.py
# ```

# Avoid:

# ```text
# my calculator.py
# ```

# because spaces make imports inconvenient.

# Also avoid naming your own module after important standard-library modules.

# For example, don't create:

# ```text
# random.py
# ```

# and then expect:

# ```python
# import random
# ```

# to always mean Python's standard-library `random` module.

# ---

# # 35. Common Import Error

# If:

# ```python
# import calculator
# ```

# gives:

# ```text
# ModuleNotFoundError
# ```

# Python couldn't find the module in its import search path.

# Check:

# 1. File name
# 2. Current project folder
# 3. Virtual environment
# 4. Package structure
# 5. Python interpreter selected in VS Code

# ---

# # 36. `ModuleNotFoundError` vs `ImportError`

# ### ModuleNotFoundError

# Python can't find the module:

# ```python
# import abc123
# ```

# ### ImportError

# The module exists, but the requested thing cannot be imported.

# Example:

# ```python
# from math import hello
# ```

# There is no `hello` in `math`.

# ---

# # 37. Circular Imports

# A circular import happens when modules depend on each other.

# ```text
# A → B
# ↑   ↓
# └───┘
# ```

# Example:

# ```python
# # a.py
# from b import function_b
# ```

# ```python
# # b.py
# from a import function_a
# ```

# This can cause import errors.

# ### Better approach

# Reorganize shared functionality into a third module:

# ```text
# common.py
# ```

# Then:

# ```text
# A → common
# B → common
# ```

# ---

# # 38. `dir()` With Modules

# You can see names available inside a module:

# ```python
# import math

# print(dir(math))
# ```

# It shows functions, constants, and other names.

# ---

# # 39. `help()`

# You can get documentation:

# ```python
# import math

# help(math)
# ```

# Or:

# ```python
# help(math.sqrt)
# ```

# ---

# # 40. Finding a Module's Location

# ```python
# import math

# print(math.__file__)
# ```

# For many Python modules this shows their location.

# Some built-in modules may not have a normal `.py` file, so `__file__` may not exist.

# ---

# # 41. Module-Level `__name__`

# Every module has:

# ```python
# __name__
# ```

# Example:

# ```python
# print(__name__)
# ```

# If you directly run:

# ```text
# test.py
# ```

# output:

# ```text
# __main__
# ```

# If imported:

# ```python
# import test
# ```

# inside `test.py`:

# ```text
# test
# ```

# ---

# # 42. `__all__`

# A module can define:

# ```python
# __all__ = ["add", "subtract"]
# ```

# This controls what names are considered public for:

# ```python
# from module import *
# ```

# Example:

# ```python
# __all__ = ["add"]

# def add(a, b):
#     return a + b

# def secret():
#     print("Secret")
# ```

# Then:

# ```python
# from calculator import *
# ```

# primarily imports the names listed in `__all__`.

# **Note:** `__all__` does not make something truly private.

# ---

# # 43. Public vs Private Names

# Convention:

# ```python
# name
# ```

# means public.

# ```python
# _name
# ```

# means:

# > Internal/private by convention.

# Example:

# ```python
# def _helper():
#     pass
# ```

# Python does not strictly enforce this privacy.

# ---

# # 44. Package `__init__.py` Can Expose Functions

# Suppose:

# ```text
# tools/
# ├── __init__.py
# └── calculator.py
# ```

# `calculator.py`:

# ```python
# def add(a, b):
#     return a + b
# ```

# You can put in `__init__.py`:

# ```python
# from .calculator import add
# ```

# Then users can write:

# ```python
# from tools import add

# print(add(2, 3))
# ```

# instead of:

# ```python
# from tools.calculator import add
# ```

# This is useful for creating a clean package interface.

# ---

# # 45. Package vs Module

# | Module               | Package             |
# | -------------------- | ------------------- |
# | Usually a `.py` file | Usually a directory |
# | Contains code        | Organizes modules   |
# | `calculator.py`      | `tools/`            |
# | Smaller unit         | Larger structure    |

# Easy memory trick:

# ```text
# Module = one toolbox
# Package = a box containing many toolboxes
# ```

# ---

# # 46. Module vs Library vs Package

# These terms are often confused.

# ### Module

# A Python file:

# ```text
# math_tools.py
# ```

# ### Package

# A collection/namespace of modules:

# ```text
# mytools/
# ├── calculator.py
# └── converter.py
# ```

# ### Library

# A broader term for reusable code.

# A library can contain modules and packages.

# For example, people commonly call NumPy a **library/package**, even though technically its distribution and internal structure are more complex.

# ---

# # 47. Example: Real Project Structure

# A larger Python project might look like:

# ```text
# my_app/
# │
# ├── main.py
# ├── requirements.txt
# │
# ├── app/
# │   ├── __init__.py
# │   │
# │   ├── database/
# │   │   ├── __init__.py
# │   │   └── db.py
# │   │
# │   ├── models/
# │   │   ├── __init__.py
# │   │   └── user.py
# │   │
# │   └── services/
# │       ├── __init__.py
# │       └── authentication.py
# │
# └── tests/
#     └── test_user.py
# ```

# Then:

# ```python
# from app.models.user import User
# from app.services.authentication import login
# ```

# This is how large applications stay organized.

# ---

# # 48. Module Import Flow

# Suppose:

# ```python
# from tools.calculator import add
# ```

# Think:

# ```text
# Python
#   ↓
# Find tools
#   ↓
# Find calculator
#   ↓
# Find add
#   ↓
# Give add to your program
# ```

# ---

# # 49. Important Difference: `import` vs `from`

# ### `import`

# ```python
# import math

# math.sqrt(25)
# ```

# The module name remains visible.

# ### `from`

# ```python
# from math import sqrt

# sqrt(25)
# ```

# You directly get the selected object.

# ---

# # 50. Best Practices

# Prefer:

# ```python
# import math
# ```

# when you want clear module ownership.

# Use:

# ```python
# from math import sqrt
# ```

# when importing a small number of well-known objects.

# Avoid excessive:

# ```python
# from module import *
# ```

# Keep modules focused:

# ```text
# database.py
# ```

# should mainly deal with database-related code.

# Use packages when a project becomes larger.

# Use virtual environments for project dependencies.

# Keep dependencies in:

# ```text
# requirements.txt
# ```

# ---

# # 51. Complete Mini Project

# ### Structure

# ```text
# calculator_project/
# │
# ├── main.py
# └── calculator/
#     ├── __init__.py
#     ├── basic.py
#     └── advanced.py
# ```

# ### `basic.py`

# ```python
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b
# ```

# ### `advanced.py`

# ```python
# def square(a):
#     return a ** 2

# def cube(a):
#     return a ** 3
# ```

# ### `main.py`

# ```python
# from calculator.basic import add, subtract
# from calculator.advanced import square, cube

# print(add(10, 5))
# print(subtract(10, 5))
# print(square(5))
# print(cube(3))
# ```

# Output:

# ```text
# 15
# 5
# 25
# 27
# ```

# ---

# # 52. The Big Picture

# ```text
# Python
# │
# ├── Module
# │   └── calculator.py
# │
# ├── Package
# │   ├── __init__.py
# │   ├── calculator.py
# │   └── converter.py
# │
# ├── Standard Library
# │   ├── math
# │   ├── os
# │   ├── json
# │   └── random
# │
# └── Third-Party Packages
#     ├── NumPy
#     ├── Pandas
#     ├── Requests
#     └── Matplotlib
# ```

# ### Most important things to remember

# ```text
# .py file                    → Module
# Folder of related modules  → Package
# import X                    → Import module/package
# from X import Y             → Import something from X
# as                           → Give an alias
# __name__                    → Module's name
# __main__                    → Directly running file
# __init__.py                 → Package initialization/interface
# pip                         → Install packages
# venv                        → Isolated project environment
# sys.path                    → Where Python searches for imports
# ```

# ### Common mistake

# Don't confuse:

# ```python
# import calculator
# ```

# with:

# ```python
# from calculator import add
# ```

# The first gives you the **module**:

# ```python
# calculator.add()
# ```

# The second gives you the **function directly**:

# ```python
# add()
# ```
