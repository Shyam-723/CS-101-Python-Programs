inventory = {"apples": 10, "bananas": 5, "oranges": 3}
prices = {"apples": 0.50, "bananas": 0.20, "oranges": 0.75}
shopping_list = ["apples", "bananas", "oranges"]

cost = 0

for item in shopping_list:
    
    items_bought = int(input(f'How many {item} do you wish to buy? \n'))

    inventory[item] = inventory.get(item) - items_bought

    cost += prices.get(item)*items_bought

print(f'The total cost of items is: ${cost}')

print(f'New Inventory is {inventory}')                
            
