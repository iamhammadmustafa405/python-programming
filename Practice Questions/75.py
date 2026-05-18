# 75: Print all prime numbers between 1 and 100
for i in range(1,101):
    is_prime = True
    
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime:
        print(i)