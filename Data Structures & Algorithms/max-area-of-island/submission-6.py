class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = 0

            area = 1
            while q:
                r, c = q.popleft()

                directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    if ((r + dr < 0) or (c + dc < 0)) or (r + dr >= rows) or (c + dc >= cols) or grid[r + dr][c + dc] == 0:
                        continue
                    q.append((r + dr, c + dc))
                    grid[r + dr][c + dc] = 0
                    area += 1

            return area
        
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea
            