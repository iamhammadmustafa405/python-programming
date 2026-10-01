# ### Shallow Copy vs Deep Copy — Like You're 10

# Imagine you have a **box inside a box**.

# ```python
# a = [[1, 2], [3, 4]]
# ```

# Think of it like:

# ```text
# a
# └── Big Box
#     ├── Small Box → [1, 2]
#     └── Small Box → [3, 4]
# ```

# ### 🟡 Shallow Copy

# ```python
# import copy

# b = copy.copy(a)
# ```

# Python makes a **new big box**, but the small boxes are still the **same**.

# ```text
# a → Big Box → [1, 2]
#               [3, 4]

# b → Big Box ──┘
# ```

# So if you change something inside a small box:

# ```python
# b[0][0] = 100
# ```

# Then:

# ```python
# print(a)
# ```

# gives:

# ```text
# [[100, 2], [3, 4]]
# ```

# Because `a` and `b` were sharing the same small box.

# ---

# ### 🟢 Deep Copy

# ```python
# import copy

# b = copy.deepcopy(a)
# ```

# Python makes a **new big box AND new small boxes**.

# ```text
# a → Big Box → [1, 2]
#               [3, 4]

# b → Big Box → [1, 2]
#               [3, 4]
# ```

# Now:

# ```python
# b[0][0] = 100
# ```

# does **not** change `a`.

# ```python
# print(a)
# ```

# ```text
# [[1, 2], [3, 4]]
# ```

# And:

# ```python
# print(b)
# ```

# ```text
# [[100, 2], [3, 4]]
# ```

# ### 🧠 Remember this

# > **Shallow copy:** New outside, same inside.
# > **Deep copy:** New outside, new inside.

# | Copy               | Outside | Inside |
# | ------------------ | ------- | ------ |
# | `b = a`            | Same    | Same   |
# | `copy.copy(a)`     | New     | Same   |
# | `copy.deepcopy(a)` | New     | New    |

# The important part is that **this problem mainly appears with nested mutable objects**, such as lists containing lists.
