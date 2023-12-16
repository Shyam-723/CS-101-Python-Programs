def get_name():
    return input("What is your name? ")

def get_operation():
    while True:
        operation = input("Would you like to add (a), subtract (s), multiply (m), or divide (d)? ")
        if operation in ["a", "s", "m", "d"]:
            return operation
        else:
            print("Invalid operation selected.")

def get_numbers():
    while True:
        try:
            num1 = float(input("What is the first number? "))
            num2 = float(input("What is the second number? "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please try again.")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    while True:
        name = get_name()
        operation = get_operation()
        num1, num2 = get_numbers()
        if operation == "a":
            result = add(num1, num2)
        elif operation == "s":
            result = subtract(num1, num2)
        elif operation == "m":
            result = multiply(num1, num2)
        elif operation == "d":
            result = divide(num1, num2)
        print("The result is:", result)
        continue_choice = input("Do you want to continue? (y/n) ")
        if continue_choice.lower() != "y":
            break

main()
