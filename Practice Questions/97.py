# 97: Write a recursive function to print all elements in the list. hint: use list and index as parameters.
list= []
for i in range(5):
    n= int(input("Enter a Number: "))
    list.append(n)
def print_element(list,index):
    if index == len(list):
        return
    else:
        print(list[index])
        print_element(list,index+1)

print_element(list,0)

# flow in simple words
# Start at index 0
# Print element
# Move to next index
# Repeat until list ends