#Asking user to input colors
color1 = input("Input the first color: ")
color2 = input("Input the second color: ")

#Checking color if color1 is red
if( color1.lower() == "red"):
    
    if(color2.lower() == "blue"):
        
        print("Color made is purple")
        
    elif(color2.lower() == "yellow"):
        
        print("Color made is orange")
        
#Checking color if color1 is blue        
elif( color1.lower() == "blue"):
    
     if(color2.lower() == "red"):
        
        print("Color made is purple")
        
     elif(color2.lower() == "yellow"):
        print("Color made is green")
        
#Checking color if color1 is yellow 
elif( color1.lower() == "yellow"):
    
    if(color2.lower() == "blue"):
        
        print("Color made is green")

else:
    print("Error, please try again")
        
    
