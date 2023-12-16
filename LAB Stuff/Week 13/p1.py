def Adding(num):
    ans = 0
    for x in num:
        ans += int(x)
    return ans

number = input("Enter a number: ")

Sum = Adding(number)

print(f'Sum of digits in {number} is {Sum}')
