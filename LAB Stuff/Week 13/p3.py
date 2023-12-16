string = input("Enter a string: ")
count_base = 0
letter_max = ""
count_new = 0
for x in range(len(string)):
    for letter in string:
        if string[x] == letter:
            count_new += 1
            
    if count_new >= count_base:
        count_base = count_new
        letter_max = string[x]
    count_new = 0

print(f'The most frequent letter is {letter_max}')


    
