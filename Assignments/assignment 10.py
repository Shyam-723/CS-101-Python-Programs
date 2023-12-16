#importing Random class
import random 

class Coin:

    def toss(self): #Constructor
        if random.randint(0,1) == 0:    #randomly chooses heads or tails
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):               #returns sideup 
        return self.__sideup

class Game:
    def __init__(self, p1name, p2name): #Constructor
        self.__p1name = p1name
        self.__p2name = p2name
        self.__winner = "g"             #Intializing variables

        my_coin = Coin()                #Calling Coin class to obtain sideup value
        my_coin.toss()
        self.__coin = my_coin.get_sideup() 

        

    def play(self): 
        choices = ["h", "heads", "t", "tails"]      #Making choice variables
        choice = "g"
        try:
            while choice not in choices:
                choice = input(f'{self.__p1name} choose Heads or Tails: ').lower()
                print(f'The coin lands on {self.__coin}')
            
        except ValueError:
            print("Invalid input \n")           #Error handling
            
        if(choice == self.__coin):              #Obtaining winner name 
              self.__winner = self.__p1name     
        else:
            self.__winner = self.__p2name
            
    def get_winner(self):
            return self.__winner            #returning winner name

#Looping menu
userchoice = "g"

while(userchoice != "quit" or userchoice != "q"):       #Looping 
    try:
        print("          Menu")
        print("Choose an option")
        print("Play game -----> 'p'")
        print("Quit ----------> 'q'")
        userchoice = input(" :: ").lower()
        
        if(userchoice == "p"):
            p1 = input("Input player 1's name: ")
            p2 = input("Input player 2's name: ")

            game = Game(p1,p2)
            game.play()
            print(f'The winner is {game.get_winner()}!\n')
            
        elif(userchoice == "q"):
            print("\nThanks for playing!")
            break

        else:
            print("Invalid input, please try again\n")
            
            
            
    except ValueError:                                      #Error handling 
        print("Invalid input, please try again \n")
    
