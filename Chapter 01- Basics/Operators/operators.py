# Arithmetic Operators.
# a= 4
# b= 3

# print(a+b)
# print(a-b)
# print(a *b)
# print(a/b)
# print(a % b)
# print(a ** b)

# relational operators.
# print(a == b)
# print(a != b) 
# print(a >=b)
# print(a>b)
# print(a<=b)
# print(a<b)


# Assignment Operators
# num = 5
# num **= 3
# print(num)

#logical operators.
# print( not True)
# print(not False)
# a= 28
# b= 34
# print( not a<b)


# And and Or Operator
a= 4
b = 4
print( a == b and a>=b)
print( a==b or a!=b)

# bit wise operators
# | Operator | Name        | Meaning                 |                   |
# | -------- | ----------- | ----------------------- | ----------------- |
# | `&`      | AND         | 1 if both bits are 1    |                   |
# | `        | `           | OR                      | 1 if any bit is 1 |
# | `^`      | XOR         | 1 if bits are different |                   |
# | `~`      | NOT         | Inverts bits            |                   |
# | `<<`     | Left shift  | Shifts bits left        |                   |
# | `>>`     | Right shift | Shifts bits right       |                   |

# Below is a **very easy, step-by-step** explanation of **Left Shift (`<<`)**, **Right Shift (`>>`)**, and **NOT (`~`)** bitwise operators.

# ---

# ## 1) Left Shift (`<<`) — *Move bits left*

# ### Simple idea

# Left shift **moves all bits to the left** and adds **0** on the right.
# Each left shift by 1 is like **multiplying by 2**.

# ---

# ### Example

# ```python
# 5 << 1
# ```

# #### Binary of 5

# ```text
# 5 = 101
# ```

# #### Shift left by 1

# ```text
# 101 → 1010
# ```

# #### Result

# ```text
# 1010 = 10
# ```

# ```python
# print(5 << 1)   # 10
# ```

# ### More examples

# ```python
# print(3 << 1)   # 6   (3 × 2)
# print(3 << 2)   # 12  (3 × 4)
# ```

# **Rule to remember:**

# ```text
# x << n  =  x × (2ⁿ)
# ```

# ---

# ## 2) Right Shift (`>>`) — *Move bits right*

# ### Simple idea

# Right shift **moves all bits to the right** and removes bits from the right.
# Each right shift by 1 is like **dividing by 2** (integer division).

# ---

# ### Example

# ```python
# 5 >> 1
# ```

# #### Binary of 5

# ```text
# 5 = 101
# ```

# #### Shift right by 1

# ```text
# 101 → 10
# ```

# #### Result

# ```text
# 10 = 2
# ```

# ```python
# print(5 >> 1)   # 2
# ```

# ### More examples

# ```python
# print(8 >> 1)   # 4
# print(8 >> 2)   # 2
# ```

# **Rule to remember:**

# ```text
# x >> n  =  x ÷ (2ⁿ)
# ```

# ---

# ## 3) NOT (`~`) — *Flip bits*

# ### Simple idea

# NOT operator **flips every bit**:

# * `1` becomes `0`
# * `0` becomes `1`

# ---

# ### Example

# ```python
# ~5
# ```

# #### Binary of 5

# ```text
# 5 = 00000101
# ```

# #### Flip bits

# ```text
# 11111010
# ```

# This becomes **-6** in Python.

# ```python
# print(~5)   # -6
# ```

# ### Easy trick (no binary needed)

# ```text
# ~x = -(x + 1)
# ```

# So:

# ```python
# ~5 = -(5 + 1) = -6
# ```

# ---

# ## One-Look Summary

# | Operator | What it does | Easy meaning  |
# | -------- | ------------ | ------------- |
# | `<<`     | Shift left   | Multiply by 2 |
# | `>>`     | Shift right  | Divide by 2   |
# | `~`      | Flip bits    | `-(x + 1)`    |

# ---

# ## Real-Life Memory Trick

# * **Left Shift (`<<`)** → number **grows**
# * **Right Shift (`>>`)** → number **shrinks**
# * **NOT (`~`)** → number becomes **negative**

# If you want, I can give **practice questions**, **MCQs**, or **real-life uses** (graphics, permissions, fast math).
