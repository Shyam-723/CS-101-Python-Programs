employees = ("Employee1", "Employee2", "Employee3", "Employee4", "Employee5")

phone_num = []

for x in employees:
    phone = input(f'Input {x} phone number: ')
    
    if(len(phone) == 10):
        phone_num.append(phone)
    else:
        print("This number can't be stored")

print(phone_num)
