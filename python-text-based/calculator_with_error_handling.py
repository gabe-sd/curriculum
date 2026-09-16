def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
            if op == 'q':
                break
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: division by zero")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator")
                continue

            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid number, try again.\n")

calculator()