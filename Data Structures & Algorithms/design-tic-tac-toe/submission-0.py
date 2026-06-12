class TicTacToe:

    # define the board
    # define the marks for each player
    # add the mark to the row and col the player wants
    # next, check if the player won
    # assume they won and disprove it in the loop
    # check rows, cols, diag and inverted diag

    def __init__(self, n: int):
        self.board = [[''] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        mark = ''
        if player == 1:
            mark = 'x'
            self.board[row][col] = 'x'
        else:
            mark = 'o'
            self.board[row][col] = 'o'

        win = True
        for c in range(self.n):
            if self.board[row][c] != mark:
                win = False
                break
        if win:
            return player
        
        win = True
        for r in range(self.n):
            if self.board[r][col] != mark:
                win = False
                break
        if win:
            return player

        win = True
        for i in range(self.n):
            if self.board[i][i] != mark:
                win = False
                break
        if win:
            return player

        win = True
        for i in range(self.n):
            if self.board[i][self.n - 1 - i] != mark:
                win = False
                break
        if win:
            return player

        return 0


        




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
