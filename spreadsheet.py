import re
class Spreadsheet:
    def __init__(self, num_rows, num_cols):
        self.board = [[''] * num_cols for i in range(num_rows)]
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.widestSize = [0] * num_cols

    def update(self, row, col, value):
        # valid row col 
        self.board[row][col] = value
        self.widestSize[col] = max([len(str(self.board[i][col])) for i in range(self.num_rows)])

    def print(self):
        for row in range(self.num_rows):
            line = '|'.join([str(i) for i in self.board[row]])
            print(line)

    def prettyPrint(self):
         for row in range(self.num_rows):
            line = '|'.join([str(self.board[row][i]).ljust(self.widestSize[i]) for i in range(self.num_cols)])
            print(line)

    def evalSum(self, query):
        pattern = r'\=sum\((\d+):(\d+)-(\d+):(\d+)\)'
        index_search = re.search(pattern, query, re.IGNORECASE)
        if index_search: 
            row1 = index_search.group(1)
            col1 = index_search.group(2)
            row2 = index_search.group(3)
            col2 = index_search.group(4)

        print(row1, col1, row2, col2)
    
s = Spreadsheet(4, 3)
s.update(0, 0, "Bob")
s.update(0, 1, 10)
s.update(0, 2, "foo")
s.update(1, 0, "alice")
s.update(1, 1, 5)
# s.print()
s.update(1, 0, "Jack")
s.prettyPrint()
s.evalSum('=sum(1:1-2:2)')