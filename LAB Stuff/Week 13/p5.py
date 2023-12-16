string = input("Enter a string: ")
string_backward = ""

def BackwardString(string):
    for x in range(len(string)):
        string_backward += string[len(string) - x - 1]
    return string_backward

print(string_backward)
