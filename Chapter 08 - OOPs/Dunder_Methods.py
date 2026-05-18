# Dunder Methods: 
class Book: 
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

b= Book("Quran")
print(b)


class MyList:
    def __init__(self,items):
        self.items = items
    
    def __len__(self): # Dunder method to return the length of the list
        return len(self.items)


l= MyList([4,5,6])
print(len(l))                        # it means:   "  l.__len__() ""



#                                                       Important!



# The confusion is normal. The key idea is:

# **You never call `__len__()` directly. Python calls it for you.**

# ---

# ## What you write vs what Python does

# When you write:

# ```python
# len(obj)
# ```

# Python internally converts it to:

# ```python
# obj.__len__()
# ```

# ---

# ## Step-by-step for your example

# ```python
# obj = MyList([1, 2, 3])
# ```

# Now when you do:

# ```python
# len(obj)
# ```

# ### Behind the scenes:

# 1. Python sees `len(obj)`
# 2. It checks: “Does `obj` have `__len__` method?”
# 3. Yes → it calls:

#    ```python
#    obj.__len__()
#    ```
# 4. That returns:

#    ```python
#    len(self.items)  # → len([1,2,3]) → 3
#    ```

# ---

# ## Why not call `__len__()` directly?

# You *can* do this:

# ```python
# obj.__len__()
# ```

# But it’s **not recommended**, because:

# * It’s not Pythonic
# * Built-in functions like `len()` are cleaner and standard
# * Python is designed to use `len(obj)`, not `obj.__len__()`

# ---

# ## Real-life analogy

# Think of it like this:

# * You press a button: `len(obj)`
# * Inside the machine, Python presses: `__len__()`

# You don’t operate the internal mechanism directly.

# ---

# ## Important Rule

# 👉 If you want your object to work with `len()`, you must define `__len__()`

# Otherwise:

# ```python
# len(obj)
# ```

# ❌ will give error:

# ```
# TypeError: object has no len()
# ```

# ---

# ## Short Summary

# * `len(obj)` → user-friendly way
# * `obj.__len__()` → internal method Python calls
# * You define `__len__` so Python knows what to do

# ---

# If you want, I can show how this works for `+`, `==`, and `print()` in the same way.
