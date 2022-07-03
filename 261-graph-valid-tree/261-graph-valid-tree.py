class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        visited = [False]*n
        adjLst = {}
        # build adjList first
        for edge in edges:
            start,end = edge
            if start not in adjLst:
                adjLst[start] = []
            if end not in adjLst:
                adjLst[end] = []
            adjLst[start].append(end)
            adjLst[end].append(start)
             
        if 0 not in adjLst:
            return False
        if self.detectCyclic(adjLst, visited, 0, -1): # cycle detected
            return False
        for b in visited: # Check if graph is connected
            if not b: # Not every node was visited, means graph is disconnected
                return False
        return True
        
        
    
    def detectCyclic(self, adjLst, visited, curr, prev):
        if visited[curr]:
            return True
        visited[curr] = True
        res = False
        for node in adjLst[curr]:
            if node == prev:
                continue
            res = res or self.detectCyclic(adjLst, visited, node, curr)
        return res
            
                
            
        