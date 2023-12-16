
def getName():
###########################
    name = input("Enter the student's name: ")  #Asking user to input a name
    return name.lower()                              #returning string value
###########################


def getScore():
###########################
    while True:
        try:
            score = float(input("Enter the student's score: "))         #First attempt to get user input
            return score
        except ValueError:
            score = float(input("Please input a valid score score: "))  #in case of wrong user input type 
            return score
###########################
    

def newScore():
###########################
    grade_file = open('gradebook.txt', 'a') #Creating & Opening a .txt file named 'gradebook' ^^^^Should I use 'a' or 'w'?^^^^

    name = getName()                        #Calling getName function
    grade_file.write(f'{name}\n')                  #Writing name in text file
    
    score = getScore()                      #Calling getScore function
    grade_file.write(f'{score}\n')                 #Writing name in text file

    grade_file.close()                      #Closing file
###########################


def readRecords():
###########################
    try:
        infile = open('gradebook.txt', 'r') #Opening gradebook.txt file to read

        grades = infile.read()              #Reading gradebook file and copying data to 'grades' variable
            
        infile.close()                      #Closing file
    
        print(grades)                       #Printing data from file that was passed to 'grades' variable

    except FileNotFoundError:
            print("Unable to open the file")
###########################


def getGrade(studentName):
###########################
    total = 0
    while True:
        
        try:
            points = float(input("Input the total number of points: "))
            break
        except ValueError:
            print("Please Enter a valid input \n")

    while True:
        try:
        
            infile = open('gradebook.txt', 'r') #Opening and reading gradebook file
            line = infile.readline()                       #Temp value for line

            for lines in line:
                
                line = line.rstrip('\n')
                
                if (line == studentName):
                    line = infile.readline()
                    
                    total = total + float(line)
                    
                else:
                    line = infile.readline()
                
            infile.close()
                    
            break      
            
        except FileNotFoundError:
            print("Unable to open the file")
            
    if((total/points)*100 >= 90):
        grade = "A"
    elif((total/points)*100 < 90 and total/points >= 80):
        grade = "B"
    elif((total/points)*100 < 80 and total/points >= 70):
        grade = "C"
    elif((total/points)*100 < 70 and total/points >= 60):
        grade = "D"
    else:
        grade = "F"
    
    return grade    

###########################

def menu():
    response = ""
    while response.lower() != "exit":
        print("\n\nWelcome to the grade book")
        print("Choose one of the following: ")
        print("Enter a new test score: <NEW>")
        print("Read all scores: <READ>")
        print("Get Student grade: <GRADE>")
        response = input(" :: ")
        if response.lower() == "read":
            readRecords()
        elif response.lower() == "new":
            newScore()
        elif response.lower() == "grade":
            name = input("Enter the student name: ")
            score = getGrade(name.lower())
            print(name + " overall score is " + str(score))
        elif response.lower() != "exit":
            print("Invalid response")
def main():
    menu()
    print("Thank you for using the gradebook")
main()
