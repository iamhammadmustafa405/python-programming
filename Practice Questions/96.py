# 96: Write a Recursive Function to calculate the sum of first n natural numbers.
def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1) + n
    
print(sum(2))