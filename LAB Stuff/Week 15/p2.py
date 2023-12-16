class Person:
    def __init__(self,name, age): #Constructor
        self.__name = name
        self.age = age

    def introduce(self):
        print("Happy birthday, " + self.__name + ". You are " + str(self.age) + " years old!") #Printing output

    def have_birthday(self):
        self.age += 1           #Increase age variable by 1

    
        

obj = Person("Shyam", 19)
obj.introduce()
print("After one year\n")

obj.have_birthday()
obj.introduce()
