def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cant Div with 0 mate"
    return x / y

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Q. Quit")

    while True:
        # We use a loop so the user can do multiple calculations
        choice = input("\nEnter your choice (1/2/3/4 or Q): ").upper()

        if choice == 'Q':
            print("Exiting calculator. Ciao!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter 1st number: "))
                num2 = float(input("Enter 2nd number: "))
            except ValueError:
                print("Invalid input! Please enter actual numbers.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Cant Div with 0 mate.":
                    print(result)
                else:
                    print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid input! Operator isnt operating.")

if __name__ == "__main__":
    calculator()