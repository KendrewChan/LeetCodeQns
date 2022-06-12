class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = self.buildAdjList(n, edges)
        
        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1: # if leaf
                leaves.append(i)

         # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop() 
                # remove the only edge left
                neighbors[neighbor].remove(leaf) # remove leaf from neighbor's edge
                if len(neighbors[neighbor]) == 1: # check if neighbor is leaf again
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves
        
    def buildAdjList(self, n, edges):
        adjList = [set() for _ in range(n)]
        for edge in edges:
            a, b = edge
            adjList[a].add(b)
            adjList[b].add(a)
        return adjList
        
        