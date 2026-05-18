# 86: Write a function that returns the sum of elements in the list.
list1= [4,5,6,7,8,9]
list2 = [5,6,7]
def sum(list):
    sum=0
    for item in list:
        sum+=item
    print(f"Sum of elements is: {sum}")


sum(list1)
sum(list2)