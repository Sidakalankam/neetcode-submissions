class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for val in row:
                if val == '.':
                    continue
                val = int(val)
                if val < 1 or val > 9 or val in seen:
                    return False
                seen.add(val)
        
        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                val = int(val)
                if val < 1 or val > 9 or val in seen:
                    return False
                seen.add(val)
        
        # Check 3x3 squares
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    val = board[row][col]
                    if val == '.':
                        continue
                    val = int(val)
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)
        
        return True          
                
            
