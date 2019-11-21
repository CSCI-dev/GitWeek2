#   Ethan Taylor
#  ​CSCI 102 – Section C
#   Week 11 - Part A

def PrintOutput(str):
    print("OUTPUT", str)

def LoadFile(path):
    file = open(path, r)
    print ("OUTPUT" + file.read().split("\n")
    file.close()
