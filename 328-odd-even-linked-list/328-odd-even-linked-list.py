# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd, even = head, head.next
        evenStart = even
        if even:
            count = 1
            curr = even.next
            while curr:
                if count % 2 == 0:  # even
                    even.next = curr
                    even = even.next
                else:               # odd
                    odd.next = curr
                    odd = odd.next
                curr = curr.next
                count += 1
            even.next = None
        odd.next = evenStart
        return head