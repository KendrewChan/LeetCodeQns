# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root and root.left == None and root.right == None:
            return (targetSum-root.val) == 0
        if not root:
            return False
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum - root.val)