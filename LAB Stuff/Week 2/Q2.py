charge = float(input("Enter meal charge : ")) #Getting input from user

Tip = (18/100)*charge   #Formulas

Tax = (7/100)*charge

Total = charge + Tip + Tax

#printing
print("Charge : " +str(charge) +"\n" +" Tip : " +str(Tip) +"\n" +" Tax : " +str(Tax) +"\n" +" Total : " +str(Total))

