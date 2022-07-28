# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = [(root,1)]
        max_length = 1
        while len(que) > 0:
            leftmost_idx = que[0][1]
            temp = []
            for item in que:
                node, index = item
                max_length = max(max_length, index-leftmost_idx+1)
                if node.left:
                    temp.append((node.left,index*2))
                if node.right:
                    temp.append((node.right,index*2+1))
            que = temp
        return max_length