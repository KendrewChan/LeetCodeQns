# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Floyd Cycle Detection
        if not head:
            return False
        normal = head
        double = head
        while double.next and double.next.next:
            # Case 1: If there wasn't a cycle, then this won't go to infinity
            # Case 2: If there's a cycle, we'll be able to find it
            normal = normal.next
            double = double.next.next
            if normal == double:
                return True
        return False