List = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Input a number less than 10: "))

def display(List,val):
    
    for val in List:
        if(val > num):
            print(val)


print(f'\n Numbers bigger than {num} are:')


val = display(List,num)




