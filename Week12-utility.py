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

def ScoreFinder(players, scores, name):
    found = False
    for index in range(len(players)):
        if players[index].lower() == name.lower() and found == False:
            print("OUTPUT", players[index], "got a score of", scores[index])
            found = True
    if(found == False):
        print("OUTPUT player not found")

def Union(a, b):
    for item in b:
        if(not item in a):
              a.append(item)
    return a

def Intersection(a, b):
    intersection = []
    for item in a:
        if item in b and not item in intersection:
            intersection.append(item)
    return intersection

def NotIn(a, b):
    aNotB = []
    for item in a:
        if not item in b:
            aNotB.append(item)
    return aNotB
