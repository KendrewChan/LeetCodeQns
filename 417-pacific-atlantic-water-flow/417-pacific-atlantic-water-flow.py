class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = [[False]*cols for _ in range(rows)]
        atlantic = [[False]*cols for _ in range(rows)]
        for i in range(rows):
            visited = [[False]*cols for _ in range(rows)]
            self.dfs(heights, pacific, visited, -math.inf, i, 0)
            visited = [[False]*cols for _ in range(rows)]
            self.dfs(heights, atlantic, visited, -math.inf, i, cols-1)
            
        for j in range(cols):
            visited = [[False]*cols for _ in range(rows)]
            self.dfs(heights, pacific, visited, -math.inf, 0, j)
            visited = [[False]*cols for _ in range(rows)]
            self.dfs(heights, atlantic, visited, -math.inf, rows-1, j)
            
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
                
        return res
    
    
    def dfs(self, heights, toCheck, visited, prevs, row, col):
        if not 0 <= row < len(heights) or not 0 <= col < len(heights[0]):
            return
        if visited[row][col]:
            return
        curr = heights[row][col]
        if curr < prevs:
            return
        toCheck[row][col] = True
        visited[row][col] = True
        up = self.dfs(heights, toCheck, visited, curr, row+1, col)
        down = self.dfs(heights, toCheck, visited, curr, row-1, col)
        left = self.dfs(heights, toCheck, visited, curr, row, col-1)
        right = self.dfs(heights, toCheck, visited, curr, row, col+1)
    
"""
[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
[[2,1],[1,2]]
[[1,2,3],[8,9,4],[7,6,5]]
"""