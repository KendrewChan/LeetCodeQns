class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = -1
        bfs = []
        # init
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    bfs.append((row,col))
        
        hadRottenOranges = True if len(bfs) > 0 else False
        while len(bfs) > 0:
            # print(bfs)
            curr = []
            for rotten in bfs:
                row, col = rotten
                curr += self.getAdjacentOrange(grid, row, col)
            minutes += 1
            bfs = curr
    
        # Check if still has fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        if minutes == -1:
            return 0        
        
        return minutes
        
        
    def getAdjacentOrange(self, grid: List[List[int]], row: int, col: int) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        up = (row+1, col)
        down = (row-1, col)
        left = (row, col-1)
        right = (row, col+1)
        adj = [up,down,left,right]
        res = []
        for t in adj:
            i, j = t
            if i < 0 or i >= rows:
                continue
            if j < 0 or j >= cols:
                continue
            if grid[i][j] != 1:
                continue
            grid[i][j] = 2 # Make rotten
            res.append(t)
        return res
                
        