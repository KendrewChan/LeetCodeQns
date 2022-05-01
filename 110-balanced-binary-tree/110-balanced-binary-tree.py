# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    depthMemo = {}
    depthMemo[None] = 0
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = self.helper(root.left)
        right = self.helper(root.right)
        return abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def helper(self, root):
        if root in self.depthMemo:
            return self.depthMemo[root]
        self.depthMemo[root] = 1 + max(self.helper(root.left),self.helper(root.right))
        return self.depthMemo[root]
        
        