# 100: Write a recursive function to find the maximum element in a list.
list= [6,7,12,78,56]
def find_max(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0],find_max(list[1:]))
        

print(find_max(list))




# ### Step-by-step thinking

# Example:

# ```python
# [3, 7, 2, 9]
# ```

# Break it:

# ```
# max([3,7,2,9]) = max(3, max([7,2,9]))
# max([7,2,9])   = max(7, max([2,9]))
# max([2,9])     = max(2, max([9]))
# max([9])       = 9   ← base case
# ```

# Now compare back:

# ```
# max(2,9) = 9
# max(7,9) = 9
# max(3,9) = 9
# ```
# Final answer = **9**
