#Professor's code used for detecting prime numbers
def prime_or_composite(n):
    has_divisor = False    
    for i in range(2, n):
        if n % i == 0:
            has_divisor = True
    if has_divisor:
        return False
    else:
        return True


#Creating files
def CreatePrimeFile():  
    index = 0                                               #Temp index variable for looping purpose

    prime_file = open('prime.txt' ,'w')                     #Creating new prime file
    while index < len(prime_list):
        
        prime_file.write(f'{prime_list[index]}\n')          #Writing prime list to file
        index += 1
    prime_file.close()                                      #Closing prime file
        
def CreateCompositeFile():
    index = 0                                               #Temp index variable for looping purposes

    composite_file = open('composite.txt' ,'w')             #Creating new composite.txt file
    while index < len(composite_list):
        
        composite_file.write(f'{composite_list[index]}\n')  #Writing composite list to file
        index +=1
    composite_file.close()                                  #Closing composite file
    

#Starting the program
    
#Loop for input validation
num = -1
while (num <= 0):
    
    try:                                                      #Error handling    
        num = int(input("Input a number greater than one: ")) #Obtaining input from user
        
    
    except ValueError: 
        print("Please input a valid number greater than one. \n")



#Creating lists
prime_list = []                                     #Creating prime list
composite_list = []                                 #Creating composite list

for i in range(2,num+1):                            #loop to obtain individual number below num

    ans = prime_or_composite(i)                     #Calling function to check if number is prime or composite

    if (ans == False):                              #If number is composite
        composite_list.append(i)                    #Adding number to composite list
        print(f'composite: {i}')                    #Printing composite number to user
        
        
    else:
        prime_list.append(i)                    #Adding number to prime list
        print(f'prime: {i}')                    #Printing prime number to user


CreatePrimeFile()
CreateCompositeFile()

            
