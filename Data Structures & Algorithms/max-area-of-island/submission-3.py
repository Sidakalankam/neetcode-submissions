class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
   

        def dfs(r, c):
            stack = [(r, c)]
            visited.add((r,c))
            area = 1
            while stack:
                row, col = stack.pop()
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        stack.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
            return area
            
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islandArea = dfs(r, c)
                    maxArea = max(islandArea, maxArea)
        return maxArea           
                    
        
        