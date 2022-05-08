/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    if root == nil {
        return true
    }
    return compare(root.Left, root.Right)
}

func compare(left *TreeNode, right *TreeNode) bool {
    if left == nil && right == nil {
        return true
    } else if left == nil || right == nil {
        return false
    }
    if left.Val != right.Val {
        return false
    }
    return compare(left.Left, right.Right) && compare(left.Right, right.Left)
}