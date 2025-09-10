# Calculator - Performs basic arithmetic operations with continuous calculation feature
def addition(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary mapping operators to their corresponding functions
operations = {
    "+": addition,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    from art import logo

    print(logo)

    n1 = float(input("What's the first number? "))

    while True:
        # Display available operations
        print("+ \n"
              "- \n"
              "* \n"
              "/ \n")
        choice = input("Pick an operation: ")

        # Validate operation choice
        while choice not in operations:
            print("Invalid operation. Choose from +, -, *, /")
            choice = input("Pick an operation: ")

        n2 = float(input("What's the next number? "))

        # Handle division by zero error
        if choice == "/" and n2 == 0:
            print("Error: cannot divide by zero!")
            continue

        # Perform calculation and display result
        result = operations[choice](n1, n2)
        print(f"{n1} {choice} {n2} = {result}")

        # Prompt to continue with result or start new calculation
        continue_or_not = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if continue_or_not == "n":
            calculator()  # Restart calculator for new calculation
            break
        else:
            n1 = result  # Use result as first number for next operation

calculator()
