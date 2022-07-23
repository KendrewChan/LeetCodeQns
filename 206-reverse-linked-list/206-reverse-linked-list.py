# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList_original(self, head):
        # Check the adapted solution before for an easier explanation
        if not head.next:
            # The "not head" is to check the initial input
            # The "not head.next" is to check we reached the last node
            return head
        curr_last = self.reverseList(head.next)
        head.next.next = head # e.g. let head == val_4, t = head.next == val_5, we assign t.next = head == val_4
        head.next = None # this is actually useful only for the first node / (last node of revresed)
        return curr_last
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This one should be easier to understand!
        if not head:
            return None
        last = self.helper(head)
        head.next = None
        return last
    
    def helper(self, head):
        if not head.next:
            # The "not head.next" is to check for when we just reached before the last node
            return head
        curr_last = self.reverseList(head.next)
        head.next.next = head # e.g. let head == val_4, t = head.next == val_5, we assign t.next = head == val_4
        return curr_last
        