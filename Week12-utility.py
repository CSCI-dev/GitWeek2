#   Ethan Taylor
#  ​CSCI 102 – Section C
#   Week 11 - Part A

def PrintOutput(str):
    print("OUTPUT", str)

def LoadFile(path):
    file = open(path, r)
    print ("OUTPUT" + file.read().split("\n"))
    file.close()

def UpdateString(string, insert, index):
    output = string[0:index] + insert + string[index+1:]
    print("OUTPUT" + output)

def FindWordCount(list, string):
    count = 0
    for substring in list:
        if substring == string:
            count += 1
    return count
