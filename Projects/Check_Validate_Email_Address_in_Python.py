# 05.Validating Email address in python. (Using String Functions)
# k,j,d=0,0,0
# email= input("Enter your Email: ")  # minimum characters in email:(g@g.in) (6 Characters)
# if len(email) >= 6: # 1
#     if email[0].isalpha(): #2
#         if ("@" in email) and (email.count("@") == 1): #3
#             if (email[-4]== ".") ^ (email[-3]== "."): # 04
#                 for i in email:
#                     if i==i.isspace(): #5
#                         k=1
#                     elif i.isalpha(): #5
#                         if i == i.upper():
#                             j=1
#                     elif i.isdigit():
#                         continue
#                     elif i == "_" or i== "." or i =="@":
#                         continue
#                     else: #5
#                         d=1

#                 if k==1 or j==1 or d==1:
#                     print("Wrong Email! 05")
#                 else:
#                     print("Right Email!")
#             else:
#                 print("Wrong Email! 04")
#         else:
#             print("Wrong Email! 03")
#     else:
#         print("Wrong Email! 02")
# else:
#     print("Wrong Email! 01")



# GUI Version

from tkinter import *

def validate_email():
    k, j, d = 0, 0, 0
    email = entry.get()
    
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."): # Using XOR Operator
                    
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1

                    if k == 1 or j == 1 or d == 1:
                        result.config(text="Wrong Email! (Rule 05)", fg="red")
                    else:
                        result.config(text="Right Email!", fg="green")
                else:
                    result.config(text="Wrong Email! (Rule 04)", fg="red")
            else:
                result.config(text="Wrong Email! (Rule 03)", fg="red")
        else:
            result.config(text="Wrong Email! (Rule 02)", fg="red")
    else:
        result.config(text="Wrong Email! (Rule 01)", fg="red")


# Window setup
root = Tk()
root.title("Email Validator")
root.geometry("400x250")
root.config(bg="#1e1e2f")

# Title
Label(root, text="Email Validator", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white").pack(pady=10)

# Entry field
entry = Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

# Button
Button(root, text="Validate", font=("Arial", 12), bg="#4CAF50", fg="white", command=validate_email).pack(pady=10)

# Result label
result = Label(root, text="", font=("Arial", 12), bg="#1e1e2f")
result.pack(pady=10)

# Run app
root.mainloop()