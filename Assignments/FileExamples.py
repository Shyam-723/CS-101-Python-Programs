def readFile(filename):
    response = ""
    while response.lower() != "exit":
        print("\n\nWelcome to the Filer App")
        print("Choose one of the following: ")
        print("Read entire file:   <ALL>")
        print("Read by Line:       <LINE>")
        print("Exit to menu:       <EXIT>")
        response = input(" :: ")
        if response.lower() == "all":
            all = readall(filename)
        elif response.lower() == "line":
            readbyline(filename)
        elif response.lower() != "exit":
            print("Invalid response")
    return

def getFilename():
    name = ""
    while name == "":
        name = input("Enter File name: ")
    return name

def readall(filename):
    try:
        infile = open(filename, "r")
        all = infile.read()
        print(all)
        infile.close()
    except FileNotFoundError:
        print("Unable to open the file")
    print("End of file")
    return all

def readbyline(filename):
    try:
        infile = open(filename, "r")
        line = infile.readline()
        for lines in line:
            print(line)
            input("Press any key for the next line")
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("Unable to open the file")
    print("End of file")
    return

def writeFile(filename):
    try:
        outfile = open(filename, "w")
        line = "bad"
        while line != "":
            line = input("Enter a line. Empty for exit\n")
            outfile.write(line)
            outfile.write("\n")
        outfile.close()
    except FileNotFoundError:
        print("Unable to open the file")
    return

def appendFile(filename):
    try:
        outfile = open(filename, "a")
        line = "bad"
        while line != "":
            line = input("Enter a line. Empty for exit\n")
            outfile.write(line)
            outfile.write("\n")
        outfile.close()
    except FileNotFoundError:
        print("Unable to open the file")
    return
def editFile(filename):
    a_file = open(filename, "r")
    list_of_lines = a_file.readlines()
    list_of_lines[1] = "Line2\n"

    a_file = open(filename, "w")
    a_file.write(list_of_lines)
    a_file.close()
def menu():
    response = ""
    while response.lower() != "exit":
        print("\n\nWelcome to the Filer App")
        print("Choose one of the following: ")
        print("Read File:      <READ>")
        print("Write to File:  <Write>")
        print("Append to File: <Append>")
        print("Edit Second Line: <Edit>")
        print("Exit:           <EXIT>")
        response = input(" :: ")
        if response.lower() == "read":
            name = getFilename()
            readFile(name)
        elif response.lower() == "write":
            name = getFilename()
            writeFile(name)
        elif response.lower() == "append":
            name = getFilename()
            appendFile(name)
        elif response.lower() == "edit":
            name = getFilename()
            editFile(name)
        elif response.lower() != "exit":
            print("Invalid response")
    return

menu()

