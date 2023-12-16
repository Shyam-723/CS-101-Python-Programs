
def UniqueString(set1,set2):

    new_set = set1 & set2
    
    return new_set
    


set1 = set(input("Input a string: "))

set2 = set(input("Inout another string: "))

print(f'Unique characters of the two strings are: \n {UniqueString(set1,set2)}')
