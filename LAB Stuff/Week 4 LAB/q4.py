#Setting up code
i=1
bugs=0

#While loop
while(i<=5):
    tempbugs = int(input(f' Input number of bugs collected on day {i} :'))
    bugs = bugs + tempbugs
    i = i + 1
print("\nNumber of bugs caught = " ,bugs)
