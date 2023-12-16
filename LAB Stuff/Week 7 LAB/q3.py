def income(A,B,C):
    income_A = A*30
    income_B = B*30
    income_C = C*30
    sales = income_A + income_B + income_C
    return sales

A = int(input("Input number of tickets sold in row A: "))
B = int(input("Input number of tickets sold in row B: "))
C = int(input("Input number of tickets sold in row C: "))

print(income(A,B,C),"$ income was made from ticket sales")
    
