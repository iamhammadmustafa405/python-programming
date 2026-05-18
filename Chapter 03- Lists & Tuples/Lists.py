# Lists
# student= ["Hammad", 18, "Azad Kashmir"]
# print(student)
# print(student[0])
# student[1] = 19
# print(student)
# print(type(student))
# print(len(student))
# marks= [78, 45, 23, 59, 47]
# print(marks[1:4]) 
# print(marks[2:len(marks)])
# print(marks[-2:])

# lists Methods.
# list= [1,5,3,4,2]
# list2= ["Gauva", "Cherry", "Apple","Mango"]
#  list.append(6)
# list2.sort()
# list.sort(reverse= True)
# print(list2)
# list.insert(3,8)
# list.remove(5)
# print(list.pop(3))
# print(list)
a = [1, 2]
a.extend([3, 4])
print(a)
# [1, 2, 3, 4]

# Below are the **most important Python list methods**, with brief explanations and examples.

# ---

# ### 1. `append()`

# Adds one item at the end of the list.

# ```python
# numbers = [1, 2, 3]
# numbers.append(4)
# # [1, 2, 3, 4]
# ```

# ---

# ### 2. `extend()`

# Adds multiple items (from another list or iterable).

# ```python
# a = [1, 2]
# a.extend([3, 4])
# # [1, 2, 3, 4]
# ```

# ---

# ### 3. `insert()`

# Inserts an item at a specific index.

# ```python
# nums = [1, 3]
# nums.insert(1, 2)
# # [1, 2, 3]
# ```

# ---

# ### 4. `remove()`

# Removes the **first occurrence** of a value.

# ```python
# nums = [1, 2, 3, 2]
# nums.remove(2)
# # [1, 3, 2]
# ```

# ---

# ### 5. `pop()`

# Removes and returns an item (default: last item).

# ```python
# nums = [1, 2, 3]
# nums.pop()
# # returns 3, list becomes [1, 2]
# ```

# ---

# ### 6. `clear()`

# Removes all items from the list.

# ```python
# nums = [1, 2, 3]
# nums.clear()
# # []
# ```

# ---

# ### 7. `index()`

# Returns the index of the first occurrence of a value.

# ```python
# nums = [10, 20, 30]
# nums.index(20)
# # 1
# ```

# ---

# ### 8. `count()`

# Counts how many times a value appears.

# ```python
# nums = [1, 2, 2, 3]
# nums.count(2)
# # 2
# ```

# ---

# ### 9. `sort()`

# Sorts the list in ascending order (in-place).

# ```python
# nums = [3, 1, 2]
# nums.sort()
# # [1, 2, 3]
# ```

# Descending:

# ```python
# nums.sort(reverse=True)
# ```

# ---

# ### 10. `reverse()`

# Reverses the list order.

# ```python
# nums = [1, 2, 3]
# nums.reverse()
# # [3, 2, 1]
# ```

# ---

# ### 11. `copy()`

# Creates a shallow copy of the list.

# ```python
# a = [1, 2, 3]
# b = a.copy()
# ```

# ---

# ### 12. `len()` *(function, not a method)*

# Returns number of elements.

# ```python
# nums = [1, 2, 3]
# len(nums)
# # 3
# ```

# ---

# ### Quick Summary Table

# | Method      | Use             |
# | ----------- | --------------- |
# | `append()`  | Add one item    |
# | `extend()`  | Add many items  |
# | `insert()`  | Add at index    |
# | `remove()`  | Delete by value |
# | `pop()`     | Delete by index |
# | `clear()`   | Remove all      |
# | `index()`   | Find position   |
# | `count()`   | Count value     |
# | `sort()`    | Sort list       |
# | `reverse()` | Reverse list    |
# | `copy()`    | Duplicate list  |

# If needed, list practice questions or tricky examples can be provided.
