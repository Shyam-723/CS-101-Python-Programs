#Asking Users for input
print("Input dimensions for Rectangle 1 ")
l1 = float(input("Enter the length of rectangle 1: "))
w1 = float(input("Enter the width of rectangle 1: "))

print("\nInput dimensions for Rectangle 2 ")
l2 = float(input("Enter the length of rectangle 2: "))
w2 = float(input("Enter the width of rectangle 2: "))

#Calculating area
a1 = l1 * w1
a2 = l2 * w2

#Comparing areas
if (a1>a2):
    print("Rectangle 1 is greater than Rectangle 2")
elif (a2>a1):
    print("Rectangle 2 is greater than Rectangle 1")
else:
    print("Rectangle 1 and Rectangle 2 have the same area")
