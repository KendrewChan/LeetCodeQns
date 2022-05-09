/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 0 {
        return nil
    }
    var mid int = len(nums)/2
    var root *TreeNode = &TreeNode{
        Val: nums[mid],
        Left: sortedArrayToBST(nums[:mid]),
        Right: sortedArrayToBST(nums[mid+1:len(nums)]),
    }
    return root
}