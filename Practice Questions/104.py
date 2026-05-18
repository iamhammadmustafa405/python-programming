# 104 Write a Program to find in which line of the file the word "learning" occur first. print -1 if not found.

# def check_for_line():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         line_count= 1
#         for line in f:
#             if word in line:
#                 print(f"The Word is found at line {line_count}") 
#                 break                                                # Iterating through the file line by line using loop.
#             line_count += 1
#         else:
#             print(-1)
# check_for_line()

# 2nd Method:
def check_for_line():
    word = input("Enter the word you want to search in the file: ")
    with open("practice.txt", "r") as f:
        data= True
        line_no =1
        while data:
            data = f.readline()
            if(word in data):
                print(f"The Word is found at line {line_no} ")
                return
            line_no +=1
    return -1

check_for_line()