from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions for BFS traversal

        # Initialize queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  # Start BFS from all rotten oranges
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0

        minutes = 0

        # Perform BFS
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check bounds and if the neighbor is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Make it rotten
                        fresh_count -= 1  # Decrease fresh orange count
                        queue.append((nr, nc))

            minutes += 1

        # If there are still fresh oranges left, return -1
        return minutes if fresh_count == 0 else -1
