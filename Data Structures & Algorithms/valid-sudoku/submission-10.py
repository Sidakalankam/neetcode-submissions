class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                b = (r // 3, c // 3)

                if num == '.':
                    continue

                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[b]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)
        
        return True
        
