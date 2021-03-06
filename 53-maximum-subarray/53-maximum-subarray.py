class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] + nums[i-1] > nums[i]):
                nums[i] = nums[i] + nums[i-1]
            maxsum = max(maxsum, nums[i])
        return maxsum