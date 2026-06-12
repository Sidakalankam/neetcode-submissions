class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(grid, r, c):
            

            q = deque()
            q.append((r, c))
            
            while q:

                r, c = q.popleft()
                
                directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
                
                for dr, dc in directions:
                    if ((r + dr < 0) or (c + dc < 0)) or (r + dr >= rows) or (c + dc >= cols) or grid[r + dr][c + dc] == '0':
                        continue
                    q.append((r + dr, c + dc))
                    grid[r + dr][c + dc] = '0'

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(grid, r, c)
                    islands += 1

        return islands