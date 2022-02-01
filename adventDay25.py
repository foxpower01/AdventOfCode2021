from math import factorial


numberOfSteps = 0
hasStepped = True
f = open("test.txt", "r")
boardstateIn = []
for line in f:
    boardstateIn.append(list(filter(lambda a: a != "\n", line)))

def canMoveEast(line, position):
    if position + 1 == len(line):
        if line[0] == ".":
            return("0")
    else:
        if line[position + 1] == ".":
            return("pos")

def canMoveSouth(nextLine, position):
    
    if nextLine[position] == ".":
        return(True)

#def canStep(line, position, nextLine, slug):
#    if slug == ">":
#        return(canMoveEast(line, position))
#    if slug == "v":
#        return(canMoveSouth(nextLine, position))

def step(boardstate):
    global hasStepped
    hasStepped = False
    for i in range(len(boardstate)):
        for j in range(len(boardstate[i])):
            if boardstate[i][j] == ">":
                if canMoveEast(boardstate[i], j) == "0":
                    boardstate[i][j] = "."
                    boardstate[i][0] = "e"
                    hasStepped = True
                if canMoveEast(boardstate[i], j) == "pos":
                    boardstate[i][j] = "."
                    boardstate[i][j + 1] = "e"
                    hasStepped = True
                   # print("moved East")
    print(boardstate)
    for i in range(len(boardstate)):
        for j in range(len(boardstate[i])):
            if boardstate[i][j] == "v":
                if i + 1 == len(boardstate):
                    if canMoveSouth(boardstate[0], j):
                        boardstate[i][j] = "."
                        boardstate[0][j] = "s"
                        hasStepped = True
                else :
                    if canMoveSouth(boardstate[i + 1], j):
                        boardstate[i][j] = "."
                        boardstate[i + 1][j] = "s"
                        hasStepped = True
                       # print("moved south")
    print(boardstate)
    for line in boardstate:
        for k in range(len(line)):
            if line[k] == "e":
                line[k] = ">"
            if line[k] == "s":
                line[k] = "v"
    #print(boardstate)
    return(boardstate)

while hasStepped == True:
#for i in range(5):
    numberOfSteps += 1
    boardstateIn = step(boardstateIn)
    print(boardstateIn)
    print(hasStepped)
print(numberOfSteps)
#print(step(boardstateIn))