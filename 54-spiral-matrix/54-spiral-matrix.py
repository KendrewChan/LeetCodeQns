class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        # Top
        top = matrix.pop(0)
        # Right
        right = []
        for i in range(len(matrix)):
            if len(matrix[i]) == 0:
                continue
            right.append(matrix[i].pop())         
        # Btm
        btm = []
        if len(matrix) != 0:
            btm = matrix.pop()[::-1]
        # Left
        left = []
        for i in range(len(matrix)):
            if len(matrix[i]) == 0:
                continue
            left.append(matrix[i].pop(0))
        left = left[::-1]
            
        return top + right + btm + left + self.spiralOrder(matrix)
    
"""
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
[[7],[9],[6]]
[[2,5,8],[4,0,-1]]
"""