class Rectangle:
    def __init__(self,width,height): #Constructor
        self.width = width
        self.height = height
        
    def Area(self):
        area = self.width * self.height #Area = width * height
        print("The area of the rectangle is: " +str(area))

    def Perimeter(self):
        perimeter = 2*(self.width + self.height) #Perimenter = 2*(length x height)
        print("The perimeter of the rectangle is: " +str(perimeter))

obj = Rectangle(10,15)
obj.Area()
obj.Perimeter()
