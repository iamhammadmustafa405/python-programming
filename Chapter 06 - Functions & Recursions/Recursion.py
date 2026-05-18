# Recursion
# print form n to 1 using recursion.
def show(n):
    if n ==0:    # ----> Base Case
        return
    print(n)
    show(n-1) # Function is calling itself
    print("Hammad")
show(5)