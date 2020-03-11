class Tictactoe:
    def __init__(self):
        self.board = [['-']*3 for i in range(3)]
        self.ai = AI(self)

    def addToken(self, row, col, token):
        self.board[row][col] = token

    def printBoard(self):
        for row in range(len(self.board)):
            print('|'.join(self.board[row]))

    def isFull(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == '-':
                    return False
        return True

    def play(self):
        while not self.isFull():
            valid = False
            while not valid:
                row = input("Enter row: ")
                col = input("Enter col: ")
                valid = self.isValidMove(row, col)
                if not valid:
                    print("It is a valid move!")
            

            self.addToken(int(row), int(col), 'X')
            self.printBoard()
            if not self.isFull():
                self.ai.makeMove()
                self.printBoard()

    def isValidMove(self, row, col):
        if row in ['0', '1', '2'] and col in ['0', '1', '2']:
            row = int(row)
            col = int(col)
            return row >= 0 and row < len(self.board) and col >= 0 and col < len(self.board[0]) and self.board[row][col] == '-'
        return False
class AI:
    def __init__(self, tictactoe):
        self.game = tictactoe

    def makeMove(self):
        if self.game.isFull():
            raise Exception("no legal move exists")
        for row in range(len(self.game.board)):
            for col in range(len(self.game.board[0])):
                if self.game.board[row][col] == '-':
                    self.game.addToken(row, col, 'O')
                    return

tictactoe = Tictactoe()
# tictactoe.addToken(0, 1, 'X')
# tictactoe.printBoard()
# ai = AI(tictactoe)
# while(True):
#     ai.makeMove()
#     tictactoe.printBoard()
tictactoe.play()