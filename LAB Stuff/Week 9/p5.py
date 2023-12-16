filename = input("Input exact name and filetype of the file you want to open: ")

try:
    infile = open(filename, 'r')

    line = infile.readline()
    while line!="":
        print(line)
        line = infile.readline()

        
except FileNotFoundError:
    print("The filename you provided doesn't exist")
    
infile.close()
    
    
