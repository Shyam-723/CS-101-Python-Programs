Sales = []
amount = 0

for x in range(1,8):
    sale = int(input(f'Inout the sales on day {x} : '))
    Sales.append(sale)


for val in Sales:
    amount = amount + val

print(Sales)
    
print(f'The total amount of income earned is: ${amount} ')
    
    
