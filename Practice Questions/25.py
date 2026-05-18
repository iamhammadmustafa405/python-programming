#25:Create a while loop that keeps asking the user for input untill they enter "Exit"
# n = input("Enter About You : ")
# while  n != "exit":
#     n= input("Enter more about You (Press Exit to Quit):").lower()


#2nd Method:
while True:
    txt= input("Enter Something (Type exit to stop): ").lower()
    if txt == "exit":
        break
    print(f"You Entered: {txt}")