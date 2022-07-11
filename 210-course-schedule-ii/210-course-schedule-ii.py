class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adjList = {}
        # build adjList
        for pre in prereq:
            course, required = pre
            # if course in adjList and required in adjList[course]:
            #     return []
            if required not in adjList:
                adjList[required] = set()
            adjList[required].add(course)
            
        return self.topologicalSort(numCourses, adjList)
        
    def topologicalSort(self, numCourses, adjList):
        # https://www.youtube.com/watch?v=eL-KzMXSXXI
        checked = [False]*numCourses
        visited = [False]*numCourses
        self.ordering = []
        self.hasCycle = False
    
        
        for at in range(numCourses):
            self.dfs(at, checked, visited, adjList)
        if self.hasCycle:
            return []
        return self.ordering
    
    def dfs(self, at, checked, visited, graph):
        if visited[at]:
            self.hasCycle = True
            return
        if checked[at]:
            return
        checked[at] = True
        visited[at] = True
        if at in graph:
            for to in graph[at]:
                self.dfs(to, checked, visited, graph)
        visited[at] = False
        self.ordering = [at] + self.ordering
                    
"""
2
[[1,0]]
4
[[1,0],[2,0],[3,1],[3,2]]
1
[]
2
[[0,1],[1,0]]
3
[[1,0],[0,2],[2,1]]
"""