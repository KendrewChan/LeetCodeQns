class Solution:    
    def longestCycle(self, edges: List[int]) -> int:
        self.cyclic = -1
        self.checked = [False]*len(edges) # used to prevent repetition
        visited = [0]*len(edges) # used for calculations
        for node in range(len(edges)):            
            self.dfs(edges, node, 0, visited)
        return self.cyclic
        
    def dfs(self, edges, node, curr, visited):
        if self.checked[node] or node == -1: # If previously checked / end of node
            return
        if visited[node] > 0:
            self.cyclic = max(self.cyclic, curr-visited[node])
            return
        visited[node] = curr
        self.dfs(edges, edges[node], curr+1, visited)
        self.checked[node] = True # There's a difference in putting this before/after the recursion
        
""" 4
[1,2,0,4,5,6,3,8,9,7]
[-1,4,-1,2,0,4]
"""