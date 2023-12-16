
name = input("Input student name: ")
netid = input("Input netid: ")
major = input("Input major: ")

info = open('student_info.txt', 'a')
info.write(f'{name}\n')
info.write(f'{netid}\n')
info.write(f'{major}\n')

info.close()
