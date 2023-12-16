while True:
    
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))


    try:
        print(f'Division of two numbers is: {num1/num2}')
        break

    except ZeroDivisionError:
        print("Zero is not a proper number as a Divisor.\n")
    
    
