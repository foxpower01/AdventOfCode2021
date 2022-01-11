def main():  
    listOfBoards = []  
    tempData = []
    output = 0
    f = open("myInputDay4part2.txt", "r")
    for line in f:
        if len(line.split(" ")) > 1:
            tempData.append(list(map(lambda x: int(x), map(lambda jtem: jtem.replace("\n", ""), filter(lambda item: item != "", line.split(" "))))))
        else:
            board = Board(tempData)
            listOfBoards.append(board)
            tempData = []
    print("hi")
    g = open("myInputDay4.txt", "r")
    listOfCalls = g.readline().split(",")
    listOfCalls = list(map(lambda x: int(x), listOfCalls))
    for n in range(0, len(listOfCalls)):
        print(n)
        j = 0
        if len(listOfBoards) > 1:
            for i in range(0, len(listOfBoards)):
                i = i - j
                print("I", i)
                listOfBoards[i].setBoardState(listOfCalls[n])
                if listOfBoards[i].hasWon():
                    listOfBoards.pop(i)
                    j += 1
                    print("len", len(listOfBoards))
        else:
            listOfBoards[0].setBoardState(listOfCalls[n])
            if listOfBoards[0].hasWon():
                print("hi")
                break
    for row in listOfBoards[0].getBoardState(): 
        print(row)
    for row in listOfBoards[0].getBoardState(): 
        for item in row:
            if item > -1:
                print(item)
                output += item
    print(output)
    print("output", output * listOfCalls[n])
    exit()
    
class Board(object):
    boardState = []

    def __init__(self, board):
        self.boardState = board
    
    def setBoardState(self, chosenNumber):
        for row in self.boardState:
            itemIndex = -1
            for item in row:
                itemIndex += 1
                if item == chosenNumber:
                    row[itemIndex] = -1
                    print(row)
    
    def getBoardState(self):
        return(self.boardState)

    def hasWon(self):
      for i in range (0, 5):
        counter = 0
        for row in self.boardState:
          if sum(row) == -5:
            return(True)
          counter += row[i]
        if counter == -5:
          return(True)


if __name__ == "__main__":
    main()
