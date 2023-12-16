def apples(x):  #This is the first function
    num = 2 * x #x is the number of juices
    print("The number of pieces of apples required are:" ,pieces(num))


def pieces(x): #This is the second function
    num = x * 4 #Here x is the number of apples
    return num


num = int(input("Input number of juices you want: "))

apples(num)
    



    
