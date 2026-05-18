# 62: print common elements between two lists.
list1= [4,6,2,3,8,4]
list2=[2,4,6,8,4,8]
list3= []
for i in list1:
    if i in list2 and i not in list3:
        list3.append(i)
        

print(list3)