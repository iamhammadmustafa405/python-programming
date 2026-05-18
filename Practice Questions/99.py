# 99: Write a recursive function to compute the sum of all elements in a list.
list= []
for i in range(5):
    n= int(input("Enter a Number: "))
    list.append(n)

def list_sum(list):
    if len(list) == 0:
        return 0
    return list[0] +list_sum(list[1:])

print(list_sum(list))
