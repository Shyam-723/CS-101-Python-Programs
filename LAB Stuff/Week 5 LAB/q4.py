factorial = 1

num = int(input("Input a number to find its factorial: "))
i = num

while(i > 0):
    factorial = factorial * i
    i = i - 1

print(f'Factorial of {num} = {factorial}')
