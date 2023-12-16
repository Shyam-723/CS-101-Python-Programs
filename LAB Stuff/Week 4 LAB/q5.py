#Getting input from user
budget=float(input("Input your budget: "))

#Loop to calculate money spent each week
i=1
cost = 0
while (i<=100):
    tempcost = float(input("Do you have any costs? \nInput 0 to terminate calculator :"))
    if(tempcost == 0):
        break
    cost = cost + tempcost
    i=i+1

#Comparing cost and budget
if(cost>budget):
    print(f'You are over budget. Your total cost is "{cost}"')
elif(budget>cost):
    print(f'Congrats! You are under budget. Your total cost is "{cost}"')
else:
    print(f'You cost and budget are equal. Your total cost is "{cost}"')
