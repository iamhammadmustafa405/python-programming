# Conditional Statements.
marks = int(input("Enter your marks: "))
if marks<0 or marks>100:
    print("Invalid Marks!")
elif marks>=90:
    print("Your Grade is A.")
    print("Congratulations.")
elif marks>= 80 and marks<90:
    print("Your Grade is B.")
    print("Congratulations.")
elif marks>= 70 and marks<80:
    print("Your Grade is C.")
    print("Congratulations.")
elif marks< 70:
    print("Your Grade is D.")

print("End of the Program.")