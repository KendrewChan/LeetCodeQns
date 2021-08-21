/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        // By checking head.next, we ensure at least 2 or more elements to be merged
        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev.next = null; // Changing slow's next to be null (to prevent cyclic dependency)
        
        // Sort the two halves
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);
        
        // Merge the sorted ones
        // At the deepest recursion it'll only be comparing 2 elements
        return merge(l1, l2);
    }
    
    ListNode merge(ListNode l1, ListNode l2) {
        ListNode beforeHead = new ListNode(0); // The next pointer on this value will be to head
        ListNode curr = beforeHead;
        
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next; // Move l1 pointer
            } else {
                curr.next = l2;
                l2 = l2.next; // Move l2 pointer
            }
            curr = curr.next;
        }
        
        if (l1 != null) curr.next = l1; // In case where l2 is empty 
        if (l2 != null) curr.next = l2; // In case where l1 is empty
        return beforeHead.next;
    }
}