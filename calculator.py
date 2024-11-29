def basic_calculator():
    while True:
        print("\nBasic Calculator \nSelect an operation \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"The result of addition: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of subtraction: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of multiplication: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division: {num1} / {num2} = {result}")

if __name__ == "__main__":
    basic_calculator()