from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Add all treasure chests (0) to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        # Directions for moving up, down, left, right
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Perform BFS
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # Check bounds and if the neighbor is a land cell (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1  # Update distance
                    queue.append((nr, nc))  # Add to queue for further exploration
