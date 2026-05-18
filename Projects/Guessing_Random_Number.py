# 01: Guessing Random Number Game:
import random

guessnum= random.randint(1,100)

while True:
    user_choice = input("Guess the Number or Quit (Q): ")
    if (user_choice == "Q" or user_choice == "Quit"):
        break
    user_choice = int(user_choice)
    if (user_choice == guessnum):
        print("You Guessed it!")
        break
    elif(user_choice < guessnum):
        print("Your Guess is too small. Make a bigger guess.")
    else:
        print("Your number is too big. make a smaller guess.")

print("------GAME OVER-------")