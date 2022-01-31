numberOfSteps = 0
hasStepped = True
f = open("myInputDay25.txt", "r")
boardstateIn = []
for line in f:
    boardstateIn.append(list(filter(lambda a: a != "\n", line)))

def canMoveEast(line, position):
    if position + 2 > len(line):
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
    hasStepped = False
    for i in range(len(boardstate)):
        for j in range(len(boardstate[i])):
            #if can(boardstate[i], j, boardstate[i + 1], boardstate[i][j]):
            if boardstate[i][j] == ">":
                if canMoveEast(boardstate[i], j) == "0":
                    boardstate[i][j] = "."
                    boardstate[i][0] = "e"
                    hasStepped = True
                    print("hi")
                if canMoveEast(boardstate[i], j) == "pos":
                    boardstate[i][j] = "."
                    boardstate[i][j + 1] = "e"
                    hasStepped = True
                    print("hi")
            if boardstate[i][j] == "v":
                if i + 1 == len(boardstate):
                    if canMoveSouth(boardstate[0], j):
                        boardstate[i][j] = "."
                        boardstate[0][j] = "s"
                        hasStepped = True
                        print("hi")
                else :
                    if canMoveSouth(boardstate[i + 1], j):
                        boardstate[i][j] = "."
                        boardstate[i + 1][j] = "s"
                        hasStepped = True
                        print("hi")

while hasStepped == True:
    numberOfSteps += 1
    step(boardstateIn)
    print(hasStepped)
print(numberOfSteps)
