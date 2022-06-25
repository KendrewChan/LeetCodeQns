# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -math.inf, math.inf)
        
    def helper(self, root, lo, hi):
        if not root:
            return True
        if not lo < root.val < hi:
            return False
        return self.helper(root.left, lo, root.val) and self.helper(root.right, root.val, hi)