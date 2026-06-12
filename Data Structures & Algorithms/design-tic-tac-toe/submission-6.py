class TicTacToe:
    # Define the board size
    # define an array for rows and cols the size of n
    # set diag and anti diag to 0
    # set the currPlayer to 1 or -1 depending on the player
    # add the current player to the rows and columns arrays based on the parameters
    # add to the diagonal and anti diagonal if it matches
    # at the end, check if the row, column or diag the player placed is equal to n
    # that way we know the current row, col, or diag is complete and we can return the player

    # this solution is the same as solution 2 but it prevents a player placing the mark in a duplicate position


    def __init__(self, n: int):
        self.board = [[' '] * n for _ in range(n)]
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] != ' ':
            return 0

        self.board[row][col] = 'x' if player == 1 else 'o'

        
        currPlayer = 1 if player == 1 else -1

        self.rows[row] += currPlayer
        self.cols[col] += currPlayer

        if row == col:
            self.diag += currPlayer
        
        if col == (self.n - row - 1):
            self.anti += currPlayer
        
        n = self.n

        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diag) == n or abs(self.anti) == n:
            return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
