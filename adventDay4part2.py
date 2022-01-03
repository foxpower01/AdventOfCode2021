def main():  
    listOfBoards = []  
    tempData = []
    gameOver = False
    output = 0
    f = open("myInputDay4part2.txt", "r")
    for line in f:
        if len(line.split(" ")) > 1:
            tempData.append(list(map(lambda x: int(x), map(lambda jtem: jtem.replace("\n", ""), filter(lambda item: item != "", line.split(" "))))))
            print(tempData)
        else:
            board = Board(tempData)
            listOfBoards.append(board)
            tempData = []
    g = open("myInputDay4.txt", "r")
    listOfCalls = g.readline().split(",")
    listOfCalls = list(map(lambda x: int(x), listOfCalls))
    while len(listOfBoards) > 1:
        for n in range(0, len(listOfCalls)):
            while len(listOfBoards) > 1:
                for board in listOfBoards:
                    board.setBoardState(listOfCalls[n])
                    if board.hasWon():
                        listOfBoards.remove(board)
                        print(len(listOfBoards))
        for row in listOfBoards[0].getBoardState(): 
            for row in board.getBoardState():
                for item in row:
                    if item > -1:
                        output += item
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
