# # Sets in Python

# A **set** is a collection of **unique values**.

# The most important characteristics are:

# 1. **Unordered** — no guaranteed position/index.
# 2. **Unique** — duplicates are automatically removed.
# 3. **Mutable** — you can add and remove elements.
# 4. **Heterogeneous** — it can contain different hashable data types.

# ---

# ## 1. Creating a Set

# Use curly braces `{}`:

# ```python
# numbers = {1, 2, 3, 4}

# print(numbers)
# ```

# Output:

# ```text
# {1, 2, 3, 4}
# ```

# ### Duplicate values are removed

# ```python
# numbers = {1, 2, 2, 3, 3, 3}

# print(numbers)
# ```

# Output:

# ```text
# {1, 2, 3}
# ```

# So:

# ```text
# {1, 2, 2, 3, 3}
#         ↓
# {1, 2, 3}
# ```

# ---

# # 2. Empty Set

# This is important:

# ```python
# x = {}
# ```

# This creates a **dictionary**, not a set.

# To create an empty set:

# ```python
# x = set()
# ```

# Check:

# ```python
# print(type(x))
# ```

# Output:

# ```text
# <class 'set'>
# ```

# ---

# # 3. Sets Are Unordered

# You should not rely on the order of elements.

# ```python
# numbers = {10, 20, 30, 40}

# print(numbers)
# ```

# A set doesn't work like a list where you have:

# ```python
# numbers[0]
# numbers[1]
# ```

# This will produce an error:

# ```python
# numbers[0]   # ❌
# ```

# Sets don't support indexing.

# ---

# # 4. Sets Are Mutable

# You can change a set after creating it.

# ```python
# numbers = {1, 2, 3}

# numbers.add(4)

# print(numbers)
# ```

# Output:

# ```text
# {1, 2, 3, 4}
# ```

# ---

# # 5. Adding Elements — `add()`

# ```python
# fruits = {"apple", "banana"}

# fruits.add("mango")

# print(fruits)
# ```

# Now the set contains:

# ```text
# apple
# banana
# mango
# ```

# If you add something that already exists:

# ```python
# fruits.add("apple")
# ```

# Nothing happens because sets contain unique values.

# ---

# # 6. Adding Multiple Elements — `update()`

# `update()` adds multiple elements.

# ```python
# numbers = {1, 2, 3}

# numbers.update([4, 5, 6])

# print(numbers)
# ```

# Output:

# ```text
# {1, 2, 3, 4, 5, 6}
# ```

# You can use another set:

# ```python
# a = {1, 2}
# b = {3, 4}

# a.update(b)

# print(a)
# ```

# Output:

# ```text
# {1, 2, 3, 4}
# ```

# ---

# # 7. Removing Elements

# There are several methods.

# ## `remove()`

# ```python
# numbers = {1, 2, 3}

# numbers.remove(2)

# print(numbers)
# ```

# Output:

# ```text
# {1, 3}
# ```

# But if the value doesn't exist:

# ```python
# numbers.remove(5)
# ```

# Python raises a `KeyError`.

# ---

# ## `discard()`

# ```python
# numbers = {1, 2, 3}

# numbers.discard(2)
# ```

# Like `remove()`, it removes an element.

# But if the element doesn't exist:

# ```python
# numbers.discard(5)
# ```

# **No error occurs.**

# ### Difference

# | Method      | If element doesn't exist |
# | ----------- | ------------------------ |
# | `remove()`  | Error                    |
# | `discard()` | No error                 |

# ---

# # 8. `pop()`

# `pop()` removes and returns **an arbitrary element**.

# ```python
# numbers = {10, 20, 30}

# x = numbers.pop()

# print(x)
# print(numbers)
# ```

# Don't assume which element will be removed.

# ---

# # 9. `clear()`

# Removes everything.

# ```python
# numbers = {1, 2, 3}

# numbers.clear()

# print(numbers)
# ```

# Output:

# ```text
# set()
# ```

# The set still exists; it is simply empty.

# ---

# # 10. `del`

# You can completely delete the set variable:

# ```python
# numbers = {1, 2, 3}

# del numbers
# ```

# Now `numbers` no longer exists.

# ---

# # 11. Checking Membership — `in`

# One of the most useful features of sets:

# ```python
# numbers = {10, 20, 30, 40}

# print(20 in numbers)
# ```

# Output:

# ```text
# True
# ```

# And:

# ```python
# print(50 in numbers)
# ```

# Output:

# ```text
# False
# ```

# You can also use `not in`:

# ```python
# print(50 not in numbers)
# ```

# Output:

# ```text
# True
# ```

# ---

# # 12. Length — `len()`

# ```python
# numbers = {10, 20, 30, 40}

# print(len(numbers))
# ```

# Output:

# ```text
# 4
# ```

# Remember that duplicates aren't counted:

# ```python
# numbers = {1, 1, 2, 2, 3}

# print(len(numbers))
# ```

# Output:

# ```text
# 3
# ```

# ---

# # 13. Looping Through a Set

# You can use a `for` loop:

# ```python
# fruits = {"apple", "banana", "mango"}

# for fruit in fruits:
#     print(fruit)
# ```

# The order is not guaranteed.

# ---

# # 14. Set Operations

# This is one of the **most important parts of sets**.

# Suppose:

# ```python
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# ```

# We can perform mathematical set operations.

# ---

# ## A. Union

# Union means:

# > **Everything from A and B, without duplicates.**

# ```python
# print(A | B)
# ```

# Output:

# ```text
# {1, 2, 3, 4, 5, 6}
# ```

# You can also use:

# ```python
# A.union(B)
# ```

# ---

# ## B. Intersection

# Intersection means:

# > **Elements that exist in both sets.**

# ```python
# print(A & B)
# ```

# Output:

# ```text
# {3, 4}
# ```

# Or:

# ```python
# A.intersection(B)
# ```

# Think:

# ```text
# A = {1, 2, 3, 4}
# B =       {3, 4, 5, 6}
#            ↑  ↑
#         common
# ```

# ---

# ## C. Difference

# `A - B` means:

# > Elements in A that are **not** in B.

# ```python
# print(A - B)
# ```

# Output:

# ```text
# {1, 2}
# ```

# But:

# ```python
# print(B - A)
# ```

# Output:

# ```text
# {5, 6}
# ```

# **Order matters for difference.**

# ---

# ## D. Symmetric Difference

# This means:

# > Elements that are in either set, but **not in both**.

# ```python
# print(A ^ B)
# ```

# Output:

# ```text
# {1, 2, 5, 6}
# ```

# The common elements `3` and `4` are removed.

# ---

# # 15. Set Operation Summary

# For:

# ```python
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# ```

# | Operation            | Symbol   | Result          |
# | -------------------- | -------- | --------------- |
# | Union                | `A \| B` | `{1,2,3,4,5,6}` |
# | Intersection         | `A & B`  | `{3,4}`         |
# | Difference           | `A - B`  | `{1,2}`         |
# | Reverse Difference   | `B - A`  | `{5,6}`         |
# | Symmetric Difference | `A ^ B`  | `{1,2,5,6}`     |

# There are also method versions:

# ```python
# A.union(B)
# A.intersection(B)
# A.difference(B)
# A.symmetric_difference(B)
# ```

# ---

# # 16. Subset

# A set is a **subset** if all of its elements exist in another set.

# ```python
# A = {1, 2}
# B = {1, 2, 3, 4}

# print(A.issubset(B))
# ```

# Output:

# ```text
# True
# ```

# You can also use:

# ```python
# A <= B
# ```

# ---

# # 17. Superset

# A set is a **superset** if it contains all elements of another set.

# ```python
# A = {1, 2, 3, 4}
# B = {1, 2}

# print(A.issuperset(B))
# ```

# Output:

# ```text
# True
# ```

# Or:

# ```python
# A >= B
# ```

# ---

# # 18. Disjoint Sets

# Two sets are **disjoint** if they have **no common elements**.

# ```python
# A = {1, 2, 3}
# B = {4, 5, 6}

# print(A.isdisjoint(B))
# ```

# Output:

# ```text
# True
# ```

# But:

# ```python
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A.isdisjoint(B))
# ```

# Output:

# ```text
# False
# ```

# because `3` exists in both.

# ---

# # 19. Set Comparison

# You can compare sets:

# ```python
# A = {1, 2, 3}
# B = {3, 2, 1}

# print(A == B)
# ```

# Output:

# ```text
# True
# ```

# Order doesn't matter.

# ```python
# [1, 2, 3] == [3, 2, 1]
# ```

# is `False` because list order matters.

# ---

# # 20. Converting List to Set

# This is a very common use.

# ```python
# numbers = [1, 2, 2, 3, 3, 4]

# unique_numbers = set(numbers)

# print(unique_numbers)
# ```

# Output:

# ```text
# {1, 2, 3, 4}
# ```

# So sets are an easy way to **remove duplicates**.

# ---

# # 21. Converting Set to List

# ```python
# numbers = {1, 2, 3}

# my_list = list(numbers)

# print(my_list)
# ```

# Now you have a list.

# Remember: the order of elements from a set should not be relied upon.

# ---

# # 22. What Can a Set Contain?

# A set can contain **hashable** objects.

# For example:

# ```python
# my_set = {10, 3.14, "Hello", True}
# ```

# This is valid.

# But a list cannot be an element of a set:

# ```python
# my_set = {[1, 2], [3, 4]}
# ```

# This gives an error because lists are mutable and therefore unhashable.

# However, a tuple can be used:

# ```python
# my_set = {(1, 2), (3, 4)}
# ```

# ---

# # 23. `frozenset`

# Python also has another set-like type called `frozenset`.

# A normal set is mutable:

# ```python
# A = {1, 2, 3}

# A.add(4)
# ```

# A `frozenset` cannot be changed:

# ```python
# A = frozenset({1, 2, 3})
# ```

# This won't work:

# ```python
# A.add(4)   # ❌
# ```

# So:

# ```text
# set       → mutable
# frozenset → immutable
# ```

# ---

# # 24. Important Set Methods

# Here's a useful cheat sheet:

# | Method                   | Purpose                            |
# | ------------------------ | ---------------------------------- |
# | `add(x)`                 | Add one element                    |
# | `update(x)`              | Add multiple elements              |
# | `remove(x)`              | Remove element; error if absent    |
# | `discard(x)`             | Remove element; no error if absent |
# | `pop()`                  | Remove arbitrary element           |
# | `clear()`                | Remove all elements                |
# | `union()`                | Combine sets                       |
# | `intersection()`         | Find common elements               |
# | `difference()`           | Find elements only in first set    |
# | `symmetric_difference()` | Find non-common elements           |
# | `issubset()`             | Check subset                       |
# | `issuperset()`           | Check superset                     |
# | `isdisjoint()`           | Check if no common elements        |

# ---

# # 25. Set vs List vs Tuple

# | Feature     | List                | Tuple            | Set                 |
# | ----------- | ------------------- | ---------------- | ------------------- |
# | Syntax      | `[ ]`               | `( )`            | `{ }`               |
# | Ordered     | Yes                 | Yes              | No guaranteed order |
# | Duplicates  | Yes                 | Yes              | No                  |
# | Mutable     | Yes                 | No               | Yes                 |
# | Indexing    | Yes                 | Yes              | No                  |
# | `in` search | Yes                 | Yes              | Yes                 |
# | Main use    | Collection of items | Fixed collection | Unique items        |

# ### The easiest way to remember

# ```text
# LIST
# [1, 2, 2, 3]
# → duplicates allowed
# → indexing allowed

# TUPLE
# (1, 2, 2, 3)
# → duplicates allowed
# → cannot change

# SET
# {1, 2, 3}
# → duplicates removed
# → no indexing
# → can change
# ```

# ### One practical example

# Suppose you have student IDs:

# ```python
# student_ids = [101, 102, 103, 101, 102, 104]
# ```

# You want only unique IDs:

# ```python
# unique_ids = set(student_ids)

# print(unique_ids)
# ```

# Result:

# ```text
# {101, 102, 103, 104}
# ```

# This is one of the most useful real-world applications of Python sets.
