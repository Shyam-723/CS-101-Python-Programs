def CombineStrings(set1,set2):

    new_set = set1 | set2
    
    return new_set



electronics_customers = {"Alice", "Bob", "Charlie", "David"}
clothing_customers = {"Charlie", "David", "Eve", "Frank"}

customers = CombineStrings(electronics_customers,clothing_customers)

print(f'Customers that have bought from this store are: \n{customers}')
