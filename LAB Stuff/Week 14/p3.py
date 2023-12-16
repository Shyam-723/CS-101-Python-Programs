
def NewDictionary(cities,temp):

    new_dic = {}
    
    for val in cities:
        
        new_dic[val] = temperatures.get(val)
        
    return new_dic

    
    


cities = ["New York", "London", "Tokyo"]

temperatures = {"New York": 70, "London": 60, "Tokyo": 80, "Paris": 55}

print(NewDictionary(cities,temperatures))
