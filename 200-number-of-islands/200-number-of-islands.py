class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        islands = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.visited[row][col] or grid[row][col] == '0':
                    continue
                self.dfs(grid, row, col)
                islands += 1
        return islands
        
    def dfs(self, grid: List[List[str]], row: int, col: int):
        if row < 0 or row >= self.rows: # Ensure row in range
            return
        if col < 0 or col >= self.cols: # Ensure col in range
            return
        if grid[row][col] == "0": # Ensure within current island boundaries
            return
        if self.visited[row][col]: # Ensure not visited
            return

        self.visited[row][col] = True
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)