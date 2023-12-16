   #Professor's code
wordIndex = {}

while True:  #Exception Handling I added
    try:
        filename = input("Enter filename for the input: ")

        infile = open(filename,"r")
        break
    
    except FileNotFoundError:
        print("Invalid filename")
    

lines = infile.readlines()

for line in lines:
    line = line.rstrip('\n')
    words = line.split()
    for word in words:
        if word in wordIndex:
            wordIndex[word] += 1
        else:
            wordIndex[word] = 1

infile.close()

############################################
#Starting my own code
userinput = "temp"  #temp value

#Starting Looping Menu
while (userinput != "quit" or userinput != "q"):
    try: 
        print("\n           Looping Menu")
        print("Choose an option: ")
        print("Find a specific word ---> (f)")
        print("Find the most seen word ---> (m)")
        print("Find the least seen word ---> (l)")
        print("Quit ---> (q)")
        userinput = input("\n :: ").lower()         #changing all input to lower case

        if(userinput == "f"):                       
            try:
                userword = input("Enter a word: ")  #User Input 
                count = wordIndex[userword]         #Checks wordIndex dictionary 
                
                print(f'The word "{userword}" appears {count} times \n\n')
                
            except KeyError:                        #Error handling
                print(f'The word "{userword}" does not appear in the text \n\n')
                

        elif(userinput == "m"):

            #temp values
            highest_word = "temp"
            highest_count = 0
            
            
            for var in wordIndex:                   #for loop to go through every key in dictionary
                if(wordIndex[var] > highest_count): #checks if value of key is greater than previous highest value
                    highest_word = var              #Updates highest key word
                    highest_count = wordIndex[var]  #Updates highest key word count
                    
            print(f'The highest word count is the word "{highest_word}" with {highest_count} counts')

        elif(userinput == "l"):
            
            #temp values
            least_word = "temp"
            least_count = 100
            
            
            for var in wordIndex:                  #for loop to go through every key in dictionary
                if(wordIndex[var] < least_count):  #checks if value of key is less than previous least value
                    least_word = var               #Updates stuff
                    least_count = wordIndex[var]
                    
            print(f'The lowest word count is the word "{least_word}" with {least_count} count')

        elif(userinput == "q"):
            print("Quit program")
            break                                   #Quits program

        else:
            print("Invalid input, please try again \n")
        
        
    except TypeError:                               #Error handling
        print("Invalid input, please try again \n")



