info = open('student_info.txt' , 'r')

name = info.readline()
netid = info.readline()
major = info.readline()

print(f' Name - {name}')
print(f' NetID - {netid}')
print(f' Major - {major}')
