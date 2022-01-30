from re import T


f = open("myInputDay25.txt", "r")
boardstate = []
for line in f:
    boardstate.append(list(filter(lambda a: a != "\n", line)))
print(boardstate)

def canMoveEast(line, position):
    if line[position + 1] == ".":
        return(True)

def canMoveSouth(nextLine, position):
    if nextLine[position] == ".":
        return(True)

#def canStep(line, position, nextLine, slug):
#    if slug == ">":
#        return(canMoveEast(line, position))
#    if slug == "v":
#        return(canMoveSouth(nextLine, position))

def step(boardstate):
    for i in range(len(boardstate)):
        for j in range(len(boardstate[i])):
            #if can(boardstate[i], j, boardstate[i + 1], boardstate[i][j]):
            if boardstate[i][j] == ">":
                if canMoveEast(boardstate[i], j):
                    boardstate[i][j] = "."
                    boardstate[i][j + 1] = ">"
            if boardstate[i][j] == "v":
                if canMoveSouth(boardstate[i + 1], j):
                    boardstate[i][j] = "."
                    boardstate[i + 1][j] = "v"
