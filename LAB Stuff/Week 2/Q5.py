price1 = float(input("What is the price of item 1? : "))

price2 = float(input("What is the price of item 2? : "))

price3 = float(input("What is the price of item 3? : "))    #Calculating prices indivdually

price4 = float(input("What is the price of item 4? : "))

price5 = float(input("What is the price of item 5? : "))


tax = (7/100)*(price1+price2+price3+price4+price5) #Calculating tax

total = tax+price1+price2+price3+price4+price5  #Calculating total

print(f' Cost of item 1: {price1}   Cost of item 2: {price2}  Cost of item 3: {price3}  Cost of item 4: {price4}  Cost of item 5: {price5} ')
print(f' Sales tax: {tax}')
print(f' Total cost: {total}')
