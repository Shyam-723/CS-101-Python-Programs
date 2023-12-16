num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: ")) #Getting input from user

#Printing options
print("Look at the following table: " +"\n" +"Enter 1 for addition" +"\n" +"Enter 2 for subtraction" +"\n" +"Enter 3 for Multipication" +"\n" +"Enter 4 for Divison")

#Getting input for option
num = int(input("Choose an option from 1 - 4 :"))

if(num==1):
    print(f'Addition value is : {num1+num2}')
elif(num==2):
    print(f'Subtraction value is : {num1-num2}')
elif(num==3):
    print(f'Multiplication value is : {num1*num2}')
elif(num==4):
    print(f'Divison value is : {num1/num2}')
else:
    print("Invalid input , please try again")
