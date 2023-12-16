name = input("Enter your full name: ")

name_list = name.split(" ")
intials = ""

for x in name_list:
    intials += x[0].upper() + ". "
    
print(intials)
