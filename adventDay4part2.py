def main():  
    listOfBoards = []  
    tempData = []
    output = 0
    f = open("test.txt", "r")
    for line in f:
        if len(line.split(" ")) > 1:
            tempData.append(list(map(lambda x: int(x), map(lambda jtem: jtem.replace("\n", ""), filter(lambda item: item != "", line.split(" "))))))
        else:
            board = Board(tempData)
            listOfBoards.append(board)
            tempData = []
    print("hi")
    g = open("test copy.txt", "r")
    listOfCalls = g.readline().split(",")
    listOfCalls = list(map(lambda x: int(x), listOfCalls))
    for n in range(0, len(listOfCalls)):
        print(n)
        if len(listOfBoards) > 1:
            for i in range(0, len(listOfBoards)):
                listOfBoards[i].setBoardState(listOfCalls[n])
                if listOfBoards[i].hasWon():
                    listOfBoards.pop(i)
                    print(len(listOfBoards))
        else:
            break
    for row in listOfBoards[0].getBoardState(): 
        for row in board.getBoardState():
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
