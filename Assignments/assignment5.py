## Shyam Gupta
## ft1685

## get random choice function
## Takes no arguments
## Returns one of three strings randomly
## To add more choices, add more strings to choices
import random
def getRandomChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

## get choice from user function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## To add more choices, add more strings to choices
def getChoice():
    choices = ['rock', 'paper', 'scissors']
    userChoice = ""
    while userChoice.lower() not in choices:
        userChoice = input("Choice rock, paper, or scissors: ")
    return userChoice.lower()

## get mode function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## Continue to prompt for choice until user enters a valid answer
## To add more choices, add more strings to choices
def getMode():
    choices = ['friend', 'computer', 'auto']
    ##################
    # YOUR CODE HERE #
    userChoice = ""
    while (userChoice.lower() not in choices):
        userChoice = input("Choose friend, computer or auto:")      
    return userChoice.lower()
    ##################


## get number function
## Input validation
## Error handling
## returns an int between 0 and max number
## Will not return an unsafe number
## Will not return negative or greater than max number
## Bad user input returns 0
def getNum(max):
    userNumber = input("Enter a number from 0 to " + str(max) + ": ")
    try:
        max = int(max)
        userInt = int (userNumber)
        if userInt > max:
            return max
        elif userInt < 0:
            return 0
        else:
            return userInt

    except ValueError:
        print("Invalid input. Returning zero")
        return 0

## get name function
## Input validation
## takes no arguments
## returns user input string
## Must not allow for a blank name
def getName():
    ##################
    # YOUR CODE HERE #
    userName = ""   #Temporary Name to intialize variable
    
    while (userName == ""): #While name is blank, as user will premsuably put something in
        userName = input("Input a name: ")
        
    return userName
        
    ##################

## get winner function
## Pass in player choices and player names as string arguments
## This function will decide the winner and give output
## Output includes displaying the players names and choices
def getWinner(p1Choice, p2Choice, p1Name, p2Name):
    ##################
    # YOUR CODE HERE #

    print()
    print(f'{p1Name} chose {p1Choice}')
    print(f'{p2Name} chose {p2Choice}')
    print()

    #If choices have rock and scissors
    if(p1Choice == "rock" and p2Choice== "scissors"):
        print(f'{p1Name} Wins!')
    elif(p2Choice == "rock" and p1Choice == "scissors"):
        print(f'{p2Name} Wins!')
          
    #If choices have Paper and Scissors    
    elif(p1Choice == "paper" and p2Choice == "scissors"):
        print(f'{p2Name} Wins!')
    elif(p2Choice == "paper" and p1Choice =="scissors"):
        print(f'{p1Name} Wins!')

    #If Choices have Rock and Paper
    elif(p1Choice == "paper" and p2Choice == "rock"):
        print(f'{p1Name} Wins!')
    elif(p2Choice == "paper" and p1Choice== "rock"):
        print(f'{p2Name} Wins!')

    #If choices are the same
    elif(p1Choice == p2Choice):
        print(" Tie Game!")
    
    ##################

## Main function 
## Prints a banner
## Calls the menu function
def main():
    print("Welcome to the Rock Paper Scissors game Version 1.01")
    menu()
    print("End of Main")

## Menu Function
## Loops on the again flag
## Validates input on prompt
## Case insensitive
## Calls play function on "yes" or "y"
## Breaks loop on "no" or "n"
## Output "invalid input" on anything else
def menu():
    ##################
    # YOUR CODE HERE #
    userChoice = ""
    max = 100
    while (userChoice.lower() != "no" or userChoice.lower() != "n"):    #Again flag
        userChoice = input("Would you like to play? Yes or No? ")
        Mode = ""
        
        if (userChoice.lower() == "no" or userChoice.lower() == "n"): #If user immediatly types no
            break
        
        
        elif(userChoice.lower() == "yes" or userChoice.lower() == "y"):
            
            Mode = getMode()
            
            games = getNum(max)
                

            for x in range (games):
                
                
                play(Mode.lower()) 

        else:
            print("invalid input")
            print()
    
    ##################

# Play function
def play(mode):
    if mode.lower() == "computer":
        p1Name = "Computer"
        p2Name = getName()
        p1Choice = getRandomChoice()
        p2Choice = getChoice()
    elif mode.lower() == "friend":
        p1Name = getName()
        p2Name = getName()
        p1Choice = getChoice()
        p2Choice = getChoice()
    elif mode.lower() == "auto":
        p1Name = "Auto P1"
        p2Name = "Auto P2"
        p1Choice = getRandomChoice()
        p2Choice = getRandomChoice()
    else:
        print("Error")
        return

    getWinner(p1Choice,p2Choice,p1Name,p2Name)
    print("Thank you for playing")

# Call main function
main()
