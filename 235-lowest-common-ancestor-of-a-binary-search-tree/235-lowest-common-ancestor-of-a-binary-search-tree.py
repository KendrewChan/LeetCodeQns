# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        # p is not necessarily smaller than q
        if p.val < q.val:
            self.helper(root,p,q)
        else:
            self.helper(root,q,p)
        return self.lca
        
    def helper(self, root, p, q):
        if root == None or self.lca != None:
            return
        
        if p.val <= root.val <= q.val:
            self.lca = root

        self.helper(root.left, p, q)
        self.helper(root.right, p, q)
        