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
    while gameOver == False:
      for i in range(0, len(listOfCalls)):
        print(i)
        listOfBoards[i].setBoardState(listOfCalls[i])
        if listOfBoards[i].hasWon():
          gameOver = True
          for row in listOfBoards[i].getBoardState():
            for item in row:
              if item > -1:
                output += item
    print(output)
    
class Board(object):
    boardState = []

    def __init__(self, board):
        self.boardState = board
    
    def setBoardState(self, chosenNumber):
        for row in self.boardState:
            for item in row:
                if item == chosenNumber:
                    item = -1
    
    def getBoardState(self):
        return(self.boardState)

    def hasWon(self):
      counter = 0
      for i in range (0, 5):
        for row in self.boardState:
          if sum(row) == -5:
            return(True)
          counter += row[i]
        if counter == -5:
          return(True)

if __name__ == "__main__":
    main()
