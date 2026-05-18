# 03. Simple Calculator
# Create a CLI calculator that performs +, -, *, /, and handles invalid inputs using try/except
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid Input!")

def get_opt():
    operators = ["+", "-", "*", "/", "%"]
    while True:
        opt= input("Enter the Operator (+, -,*,/,%): ").strip()
        if opt in operators:
            return opt
        print("Invalid Operator.Please Enter from (+,-,*,/,%) ")


def calculate(num1, num2, opt):
        if opt == "+":
            return num1 + num2
        elif opt == "-":
            return num1 - num2
        elif opt == "*":
            return num1 * num2
        elif opt == "/":
            if num2 == 0:
                raise ZeroDivisionError("Divison by zero is not allowed!")
            return num1 / num2
        elif opt == "%":
            if num2 ==0:
                raise ZeroDivisionError("Divison by zero is not allowed!")
            return num1 % num2

def main():
    print("=" * 35)
    print("CLI CALCULATOR BY M. HAMMAD MUSTAFA")
    print("=" * 35)
    while True:
        num1 = get_number("Enter 1st Number: ")
        num2 = get_number("Enter 2nd Number: ")
        opt= get_opt()
        try:
            result= calculate(num1, num2, opt)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue

        if result.is_integer():
            print(f"{num1} {opt} {num2} = {int(result)}")
        else:
            print(f"{num1} {opt} {num2} = {result:.4f}")
        

        again= input("Do you want to perform more (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()