class Student:
    def __init__(self,name,age,grades): #Constructor
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self):
        self.grades.append(85) #Adding grade of 85 to the list

    def average_grade(self):
        avg = 0
        for val in self.grades: #Calculating sum of all grades
            avg += val

        avg = avg / len(self.grades) #Dividing sum by number of grades to get average

        print("The average grade of " +self.name +" is " +str(avg)) #Printing statement


obj = Student("Shyam",19,[95,100,90])

print("Before adding new grade")
obj.average_grade()

print("\nAfter adding new grade")
obj.add_grade()
obj.average_grade()


    
            
