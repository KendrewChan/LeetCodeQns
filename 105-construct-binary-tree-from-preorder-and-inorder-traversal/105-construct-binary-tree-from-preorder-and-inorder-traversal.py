# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
        # If you read the cpp solution, it's actually the same, this is just the shortened version
        if inorder:
            ind = inorder.index(preorder.pop(0)) # Pop root first
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind]) # Settle all the left nodes first
            root.right = self.buildTree(preorder, inorder[ind+1:]) 
            return root