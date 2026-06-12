class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Loop through the grid and at each point, when we come across a 1, we run dfs
        # The dfs algorithm goes through all the nodes and counts up how many there are and updates them to be 0 so we don't revisit
        # in our main function, we can then call dfs when we see a 1 and calculate the current area vs the max area returned
        # we then return the max area we found

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0) or (r == rows or c == cols):
                return 0
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + (
                dfs(r + 1, c) +
                dfs(r - 1, c) + 
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )


        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea




