def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operator"

        return f"Result: {result}"

    except ValueError:
        return "Error: Invalid input. Please enter the stuepid numbers."

# Run the calculator
print(calculator())
