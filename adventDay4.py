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
    for n in range(0, len(listOfCalls)):
      for board in listOfBoards:
        board.setBoardState(listOfCalls[n])
        if board.hasWon():
          print("hi")
          gameOver = True
          for row in board.getBoardState():
            for item in row:
              if item > -1:
                output += item
          print("output", output * listOfCalls[n])
          exit()      
  print("output", output)
    
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
          print("row", sum(row))
          if sum(row) == -5:
            return(True)
            print("has won true")
          counter += row[i]
        print("column", counter)
        if counter == -5:
          return(True)
          print("has won true")


if __name__ == "__main__":
    main()
