class Student:
    def __init__(self,name): #Constructor
        self.name = name
        

    def get_name(self):             
        print("Your name is " + self.name) #Prints name

obj = Student("Shyam")
obj.get_name()
      
