# Name: Shyam Gupta
#NetID : ft1685

#importing Function
# PROVIDED CODE
# The following code is provided for your use
# Do not make any changes to it or remove
# See the example below to understand how to use
# this example function.
import random
def rpsChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
# End of provided code

#Gathering input on type of game

print("Rock Papers Scissors Game")
Game_type = input("Play agaisnt Friend or the Computer? Enter F or C: ")
choice1 = ""
choice2 = ""
player1 = ""
player2 = ""



#Code for if game type is with friend

if(Game_type.upper() == "F"):
    player1 = input("Enter name for player 1 : ")
    player2 = input("Enter name for player 2 : ")

    choice1 = input(f'{player1} choose Rock, Paper or Scissors: ')
    choice2 = input(f'{player2} choose Rock, Paper or Scissors: ')
    
#Code for if game type is with Computer
    
elif(Game_type.upper() == "C"):
    player1 = "Computer"
    player2 = input("Enter name for player 2 : ")
    choice1 = rpsChoice()
    choice2 = input(f'{player2} choose Rock, Paper or Scissors: ')

else:
    print("Invalid Game Type ")
    
#Output screen
print(f'{player1} chose {choice1}')
print(f'{player2} chose {choice2}')
print("")

#Deciding who wins and output

#If choices have Rock and Scissors
if(choice1.lower() == "rock" and choice2.lower()== "scissors"):
    print(f'{player1} Wins!')
elif(choice2.lower() == "rock" and choice1.lower()== "scissors"):
    print(f'{player1} Wins!')
          
#If choices have Paper and Scissors    
elif(choice1.lower() == "paper" and choice2.lower()== "scissors"):
    print(f'{player2} Wins!')
elif(choice2.lower() == "paper" and choice1.lower()=="scissors"):
    print(f'{player1} Wins!')

#If Choices have Rock and Paper
elif(choice1.lower() == "paper" and choice2.lower()== "rock"):
    print(f'{player1} Wins!')
elif(choice2.lower() == "paper" and choice1.lower()== "rock"):
    print(f'{player2} Wins!')

#If choices are the same
elif(choice1.lower() == choice2.lower()):
    print(" Tie Game!")

#If input is wrong
else:
    print("Wrong Input")
    
