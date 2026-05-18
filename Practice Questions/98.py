# 98: Write a recursive function to find the nth number in the Fibonacci sequence.
def fabii(n):
    if n== 0:
        return 0   # base case 01
    elif n==1:
        return 1  # ---. base case 02
    else: 
        return fabii(n-1) + fabii(n-2)   # ----> function call (Recursivity)
    
print(fabii(7))