def Sum(n):
    if n<1:
        return 0
    else:
        return(n + Sum(n-1))
    
    
    
num = int(input("Enter a number: "))

print(f'Factorial of {num} is {Sum(num)}')

    
