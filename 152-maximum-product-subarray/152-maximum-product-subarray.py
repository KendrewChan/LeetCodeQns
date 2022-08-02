class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curr_max = 0
        neg, pos = 0, 0
        for num in nums:
            if num < 0:
                neg, pos = min(num, pos * num), neg * num
            else:
                pos = max(num, pos * num)
                neg *= num
            curr_max = max(curr_max, pos)
        return curr_max
                