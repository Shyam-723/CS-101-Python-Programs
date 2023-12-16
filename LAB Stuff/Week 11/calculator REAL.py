def add(x,y):
    result = x+y
    return result

def sub(x,y):
    result = x-y
    return result

def mul(x,y):
    result = x*y
    return result

def div(x,y):
    result = x/y
    return result

while True:
    # Get user's name
    name = input("What is your name? ")

    choices = ["a","s","m","d"]
    userchoice = ""

    try:
        # Get operation from user
        while userchoice not in choices:
            userchoice = input("Would you like to add (a), subtract (s), multiply (m), or divide (d)? ")
            if userchoice not in choices:
                print("Invalid Input")
                
    except ValueError:
        print("Invalid input. Please try again.")


    while True:
        try:
            # Get numbers from user
            num1 = float(input("What is the first number? "))
            num2 = float(input("What is the second number? "))
            break
        except ValueError:
            print("Invalid input. Please try again.")


    if userchoice.lower() == "a":
        result = add(num1,num2)
    elif userchoice.lower() == "s":
        result = sub(num1,num2)
    elif userchoice.lower() == "m":
        result = mul(num1,num2)
    elif userchoice.lower() == "d":
        result = div(num1,num2)
    else:
        print("Invalid operation selected.")

    print(f'Result is {result}')
    
    choice = ["y","n"]
    while userchoice.lower() not in choice:
        userchoice = input("Do you want to continue? (y/n)")
        if userchoice.lower() == "y":
            break
        else:
            print("Thank you!")
                  
    if userchoice == "n":
        break
                
    
    
    
