#Asking user input
weight = float(input("Input weight of package: "))

#Printing price based on weight
if(weight<=2):
    print("Price of shipping : $" ,1.50*weight)
elif(weight>=2 and weight <=6):
      print("Price of shipping : $" ,3.00*weight)
elif(weight>=6 and weight <=10):
      print("Price of shipping : $" ,4.00*weight)
else:
      print("Price of shipping : $" ,4.75*weight)

      
      
      
