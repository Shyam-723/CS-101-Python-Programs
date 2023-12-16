def compare(n1,n2):
    if(n1>n2):
        return n1
    elif(n2>n1):
        return n2
    else:
        print("Numbers are equal!")


n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))
print(compare(n1,n2))
