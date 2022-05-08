/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    var stk []int
    var curr *ListNode = head
    for curr != nil {
        stk = append(stk, curr.Val)
        curr = curr.Next
    }
    curr = reverseList(head)
    fmt.Println(stk)
    for _, value := range stk {
        if value != curr.Val {
            return false
        }
        curr = curr.Next
    }
    return true
}

func reverseList(head *ListNode) *ListNode {
    var prev, curr *ListNode = nil, head
    for curr != nil {
        curr.Next, prev, curr = prev, curr, curr.Next
    }
    return prev
}