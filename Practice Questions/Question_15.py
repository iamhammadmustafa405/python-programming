# Question - 15: Write a program to ask the user to enter the name of their 3 favourite Tv serials and store them in a list.
ser1= input("Enter 1st serial: ")
ser2= input("Enter 2nd serial: ")
ser3= input("Enter 3rd serial: ")
tv_serials= [ser1, ser2, ser3]
print(f"The list of the Tv serials is: {tv_serials}")
# 2nd Method
serials= []
serials.append(input("Enter 1st serial:"))
serials.append(input("Enter 2nd serial:"))
serials.append(input("Enter 3rd serial:"))
print(f"The list of the Tv serials is: {serials}")

