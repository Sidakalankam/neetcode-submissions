class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        visited.add((0,0))
        q = collections.deque()
        q.append((0,0))

        length = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length

                neighbors = [[0,1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (r + dr < 0 or c + dc < 0) or (r + dr == rows or c + dc == cols):
                        continue
                    if ((r + dr, c + dc) in visited) or (grid[r + dr][c + dc] == 1):
                        continue

                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

            length += 1

        return -1


