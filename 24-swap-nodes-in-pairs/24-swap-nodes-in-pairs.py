# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        newHead = None
        curr = head
        prev = None
        prevprev = None
        while curr:
            if count % 2 == 1:
                if newHead == None:
                    newHead = curr
                curr.next, prev.next = prev, curr.next
                if prevprev != None:
                    prevprev.next = curr
                if prev != None:
                    prevprev = curr
                curr = prev.next
            else:
                if prev != None:
                    prevprev = prev
                prev = curr
                curr = curr.next
            count += 1
        if not newHead:
            return prev
        return newHead
        