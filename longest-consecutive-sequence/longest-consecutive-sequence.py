class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxi = 0
        for i in nums:
            if i-1 not in nums:
                y = i+1
                while (y in nums):
                    y += 1 
                maxi = max(maxi, y-i)
        return maxi