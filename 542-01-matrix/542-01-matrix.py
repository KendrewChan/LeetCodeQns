class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        dist = [[sys.maxint-(10**4) for _ in range(col)] for _ in range(row)]
        
        # Check top-down-rightwards
        for i in range(row):
            for j in range(col):
                if not mat[i][j]:
                    dist[i][j] = 0
                    continue
                if i > 0: # Separate checking logic
                    dist[i][j] = min(dist[i][j], dist[i-1][j]+1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1]+1)

                    
        # Check btm-up leftwards
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                # No longer need to check for mat[i][j] since it was done in line 15
                if i < row-1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j]+1)
                if j < col-1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1]+1)
                
        return dist
