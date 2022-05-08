func missingNumber(nums []int) int {
    var curr int
    for i := 0; i < len(nums); i++ {
        curr += i
        curr -= nums[i]
    }
    curr += len(nums)
    return curr
}