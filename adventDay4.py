def main():  
    listOfBoards = []  
    tempData = []
    counter = 0
    f = open("myInputDay4part2.txt", "r")
    for line in f:
        if len(line.split(" ")) > 1:
            tempData.append(list(map(lambda jtem: jtem.replace("\n", ""), filter(lambda item: item != "", line.split(" ")))))
            print(tempData)
        else:
            board = Board(tempData)
            listOfBoards.append(board)
            tempData = []
    print(listOfBoards[-1].getBoardState())
    
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

if __name__ == "__main__":
    main()