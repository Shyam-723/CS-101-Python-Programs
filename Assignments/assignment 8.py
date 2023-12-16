
#For the intial words.txt file, I only used the first few lines from your intial file

# PigLating conversion function
def PigLatin(sentence):

    vowels = ['a','e','i','o','u','y']             #List of vowels

    sentenceList = sentence.split()                #Splitting the line from inital English file into separate words 

    #Three temp variables
    tempsentence = ""
    tempword = ""
    tempconsonent = ""
    
    for string in sentenceList:                    #For loop to enter strings in list
       
        
        for letter in string:                      #For loop to enter individual letters in each string
            
            if letter in vowels:                   #Program should stop collecting consonents if letter is a vowel
                break
            
            tempconsonent += letter                #Taking note of inital consonents
                
        string = string.replace(tempconsonent, "") #removes inital consonents by replacing them with nothing
        
        tempword = string + tempconsonent + "ay " #Creates the pig latin word
        
        tempconsonent = ""                         #Resetting the tempconsonent so it doesn't cross over to other words
        
        tempsentence += tempword                   #Writes the entire inital english sentence in pig latin

        
    return tempsentence                             #Returns the pig latin sentence
                
          
                
    
while True: #Loops if filename is wrong
    try:
        file = input("Enter the filename.txt: ")    #Asking user for filename
        
        readfile = open(file,'r')                   #Opening file to read english
        appendfile = open('piglatin.txt','w')       #Opening new file to write in piglatin
        
        
        english = "g"                               #Intial variable
        
        while english != "":                        #Reads until file hits end
            
            english = readfile.readline()           #Program reads english line
            
            pig_latin_sentence = PigLatin(english)  #Program obtains pig latin version of english line
            
            appendfile.write(pig_latin_sentence + '\n') #Program writes pig latin version into appropriate file 
            
        readfile.close()
        appendfile.close()                          #Close files
        print("File sucessfully created! ")         #Confirmation to User program worked
        break       

    except FileNotFoundError:                       #Error handling
        print("Error! File Not Found! \n")


        

        
        
        
    




