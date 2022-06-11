# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal of BST is an array sorted in the ascending order.
        # instead of doing recursively, we can do iteratively
        stk = []
        while True:
            while root != None:
                stk.append(root) # if current node is left node, this will immediately get popped later on
                root = root.left # go all the way left, and append everything along the way
            # At this pt, root == None
            root = stk.pop() # Reassign with leftmost in current tree
            k -= 1
            if k == 0:
                return root.val
            root = root.right
                # Case 1: root.right == None, in that case, we'll just continue to pop from stk
                # Case 2: root.right != None, int that case we'll loop and append the left elements again