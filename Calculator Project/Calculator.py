def addition(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

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
        print("+ \n"
              "- \n"
              "* \n"
              "/ \n")
        choice = input("Pick an operation: ")

        while choice not in operations:
            print("Invalid operation. Choose from +, -, *, /")
            choice = input("Pick an operation: ")

        n2 = float(input("What's the next number? "))

        if choice == "/" and n2 == 0:
            print("Error: cannot divide by zero!")
            continue

        result = operations[choice](n1, n2)
        print(f"{n1} {choice} {n2} = {result}")

        continue_or_not = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
                                 f"").lower()

        if continue_or_not == "n":
            calculator()
            break
        else:
            n1 = result

calculator()