from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for relation in prerequisites:
            nxt, prev = relation
            d[prev].append(nxt)
        
        checked = [False] * numCourses
        visited = [False] * numCourses
        for curr in range(numCourses):
            if self.isCyclic(curr, d, visited, checked):
                return False
        return True
    
    def isCyclic(self, curr, d, visited, checked):
        if checked[curr]: # Checked nodes should not form cycle
            return False
        if visited[curr]:
            return True
        visited[curr] = True
        
        # backtrack
        ret = False
        for adj in d[curr]:
            ret = self.isCyclic(adj, d, visited, checked)
            if ret:
                break
        
        checked[curr] = True
        visited[curr] = False
        return ret
         
                