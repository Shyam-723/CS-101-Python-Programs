months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

userinput = input("Enter the date in the format mm/dd/yyyy : ")


split = userinput.split("/")
print(split)

month = int(split[0])
month = months[month-1]

day = int(split[1])
year = int(split[2])

print(f'{month} {day}, {year}')
