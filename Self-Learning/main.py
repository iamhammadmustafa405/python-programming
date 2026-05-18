# Simple dictionary...
word= input("Enter the Word: ").lower()
dict ={ "Appetite": "Hunger"
,"throw": "drop",
}
if word in dict:
    print(f"The Meaning of {word} is: {dict[word]}")