# Question - 16: Write a program to check if a list contains a palindrome of elements.
list= [1,2,3,4,1]
list2 = list.copy()
print(list2)
list2.reverse()
if list == list2:
    print("This list contains palindrome of elements.")
else:
    print("This list  doesn't contain palindrome of elements.") 