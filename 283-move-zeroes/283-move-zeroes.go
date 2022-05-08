func moveZeroes(nums []int)  {
    var frontIdx int
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[i], nums[frontIdx] = nums[frontIdx], nums[i]
            frontIdx++
        }
    }
}