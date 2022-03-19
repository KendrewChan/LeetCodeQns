class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return nums[0]
        
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-1], nums[i]+nums[i-2])
            nums[i-1] = max(nums[i-1], nums[i-2])
        return max(nums[-1], nums[-2])