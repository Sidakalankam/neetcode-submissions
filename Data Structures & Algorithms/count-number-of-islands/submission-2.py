class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through the matrix
        # at each element, if the element is a 1 run dfs
        # so we have a vistied set
        # to make sure we don't recheck the same island, when we loop, we check if the current element is a 1 and if it's not in the set
        # only then will we run dfs
        # every time we run dfs, we will add to the count by 1

        # for the dfs here are the steps:
        # the base cases are 
            # 1. that (r,c) is out of bounds
            # 2. r,c is in visited
            # 3. we check if grid[r][c] is 0 if so we return none

        # after we check base cases we just add to the visited set and recursively check all 4 directions
        # we don't need to backtrack since we're just visting each cell once
        



        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            
            if (r < 0 or c < 0) or (r == rows or c == cols):
                return
            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        islands = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands

