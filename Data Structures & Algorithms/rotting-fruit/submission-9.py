class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source bfs
        # we first loop through the grid and find all the cells with 2
        # and in that loop, we count the number of fresh oranges and initialize that as well
        # we add all those to our queue and visited set
        # we then initialize a minutes variable to 0
        # then we loop through the queue and popleft the cells and then we explore all 4 directions
        # in those 4 directions if it's valid, we change the value at that cell to 2 and decrement the fresh oranges by 1
        # and we increment the minutes by 1 for the level
        # finally we return the minutes if fresh oranges == 0 else - 1


        rows, cols = len(grid), len(grid[0])

        q = deque()


        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in dirs:
                    if (r + dr < 0 or c + dc < 0) or (r + dr >= rows or c + dc >= cols):
                        continue
                    if grid[dr + r][dc + c] == 2 or grid[dr + r][dc + c] == 0:
                        continue
                    
                    grid[dr + r][c + dc] = 2
                    fresh -= 1

                    q.append((dr + r, dc + c))

            minutes += 1

        
        return minutes if fresh == 0 else -1
                    


                


            
                