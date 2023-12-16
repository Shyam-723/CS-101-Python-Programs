def cost(x):
    cost = 0
    if (x<20):
        cost = (5 * x)
    elif (x >= 20 and x < 120):
        cost = (3.25 * x)
    else:
        cost = (1.90 * x)
    return cost

num = float(input("Input the number of copies you want: "))

print("Cost of the papers is : $" ,cost(num))
