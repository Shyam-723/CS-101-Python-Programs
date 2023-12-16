import random

states = {'Texas':'austin',  'California':'sacremento', 'Florida': 'tallahassee', 'Alabama':'montgomery', 'Alaska':'juneau'}

count = 0

for key in range(5):

    state, capital = random.choice(list(states.items()))
    
    userinput = input(f'What is the capital of {state}? \n')

    if userinput.lower() == capital:
        count += 1

print(f'You got {count}/5 correct!')
