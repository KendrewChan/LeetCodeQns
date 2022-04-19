class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximal = nums[0]
        for i in range(1,len(nums)):
            if nums[i]:
                nums[i] += nums[i-1]
                maximal = max(maximal, nums[i])
        return maximal