class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        
        for row in board:
            row_visit = set()
            for val in row:
                if val == ".":
                    continue

                if val.isnumeric():
                    if int(val) > 9 or int(val) < 1:
                        return False
                    if val in row_visit:
                        return False
                row_visit.add(val)


        
        for c in range(cols):
            col_visit = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c].isnumeric():
                    if int(board[r][c]) > 9 or int(board[r][c]) < 1:
                        return False 
                    if board[r][c] in col_visit:
                        return False
                
                col_visit.add(board[r][c])

        
        for box_row in range(0, rows, 3):
            for box_col in range(0, cols, 3):
                box_visit = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                            if board[r][c] == ".":
                                continue
                            if board[r][c].isnumeric():
                                if int(board[r][c]) > 9 or int(board[r][c]) < 1:
                                    return False 
                                if board[r][c] in box_visit:
                                    return False
                            box_visit.add(board[r][c])

        return True
                        

        


        

        



