class TicTacToe:
    # Define the board size
    # define an array for rows and cols
    # set diag and anti diag to 0


    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        currPlayer = 1 if player == 1 else -1

        self.rows[row] += currPlayer
        self.cols[col] += currPlayer

        if row == col:
            self.diag += currPlayer
        
        if col == (len(self.cols) - row - 1):
            self.anti += currPlayer
        
        n = self.n

        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diag) == n or abs(self.anti) == n:
            return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
