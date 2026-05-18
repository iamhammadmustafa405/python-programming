# #19: Write a Program using a while loop to print numbers from 1 to 10.
# a = 1
# while a<=10:
#     print(a)
#     a+=1


Simple Calculator — Improved

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operator():
    operators = ["+", "-", "*", "/", "%"]
    while True:
        opt = input("Operation (+, -, *, /, %): ").strip()
        if opt in operators:
            return opt
        print("Error: Invalid operator. Choose from +, -, *, /, %")

def calculate(num1, num2, opt):
    if opt == "+":
        return num1 + num2
    elif opt == "-":
        return num1 - num2
    elif opt == "*":
        return num1 * num2
    elif opt == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2
    elif opt == "%":
        if num2 == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        return num1 % num2

def main():
    print("=" * 35)
    print("       Simple CLI Calculator")
    print("=" * 35)

    while True:
        try:
            num1 = get_number("Enter number 1: ")
            num2 = get_number("Enter number 2: ")
            opt = get_operator()

            result = calculate(num1, num2, opt)

            # Clean output: show int if result is a whole number
            if result == int(result):
                print(f"Result: {num1} {opt} {num2} = {int(result)}")
            else:
                print(f"Result: {num1} {opt} {num2} = {result:.4f}")

        except ZeroDivisionError as e:
            print(f"Math Error: {e}")

        finally:
            print("-" * 35)

        again = input("Another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()