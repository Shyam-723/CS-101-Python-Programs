students = ("Student1", "Student2", "Student3", "Student4", "Student5")

birthyear = []
for x in students:
    year = int(input(f'Input the year {x} was born: '))
    birthyear.append(year)

for x in birthyear:
    if (x > 2000):
        print(x)
        
