def main():    
    
    print("hello")
    

class Board(object):
    boardState = []

    def __init__(self, board):
        self.boardState = board
    
    def setBoardState(chosenNumber):
        for row in boardState:
            for item in row:
                if item == chosenNumber:
                    item = -1


if __name__ == "__main__":
    main()