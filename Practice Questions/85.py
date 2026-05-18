# 85: Create a function that returns the length of a list (without using len()).
list1= [2,3,4,5,6,7,8,10]
list2= [4,5,6]
def length(list):
    len= 0
    for item in list:
        len+=1
    print(f"The Length of the List is: {len}")

length(list1)
length(list2)