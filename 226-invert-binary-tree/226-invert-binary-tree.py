# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root
    
    def helper(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.helper(root.left)
        self.helper(root.right)