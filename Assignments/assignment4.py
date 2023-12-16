# Name : Shyam Gupta    NetID: ft1685


#Setting up variables
message = ""
output = ""

#Gathering input from user
shift = int(input("Input number of shifts for encryption: "))
mode = input("Inpute encrypt or decrypt for their respective modes: ")

#Code for encryption
if(mode == "encrypt"):
    message = input("Input message to be converted: ")
    
    
    for i in message:   #Starting encryption loop, each letter will be shifted one at a time. 

            if( ord(i)>=65 and ord(i) <= 90 ): #Checking to see if letter is in lowercase
            
                output += chr( (ord(i) + shift - 65) % 26 + 65) 

            elif(ord(i) >= 97 and ord(i) <= 122): #Checking to see if in upper case
                    
                    output += chr( (ord (i) + shift - 97) % 26 + 97)
            else:
                 output += i

#Code for decryption
elif(mode == "decrypt"):
    message = input("Input message to be converted: ")
    
    shift_decrypt = 26 - shift

    for i in message: #Starting decryprtion loop
            
             if( ord(i)>=65 and ord(i) <= 90 ): #Checking to see if letter is in lowercase
           
                output += chr( (ord(i) + shift_decrypt - 65) % 26 + 65 ) 

             elif(ord(i) >= 97 and ord(i) <= 122):
                 
                 output += chr( (ord (i) + shift_decrypt - 97) % 26 + 97)
                 
             else:
                output += i

#Printing output
print(f'Original message = {message}')

print(f'New shifted message = {output}')


    

        
            
        
        
