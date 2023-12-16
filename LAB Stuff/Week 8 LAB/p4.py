import random

def quiz():
    num1 = random.randint(1,99)
    num2 = random.randint(1,99)
    ans = num1 + num2
    guess = int(input(f'What is {num1} + {num2} ? : '))

    if (guess == ans):
        print("Congratulations! You are correct! ")
    else:
        print(f'Incorrect. The correct answer is {ans}')

quiz()


