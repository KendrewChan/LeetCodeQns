class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = -99
        maxpdt = 1
        minpdt = 1
        for num in nums:
            if num < 0:
                maxpdt, minpdt = minpdt, maxpdt
            maxpdt = max(num, maxpdt * num)
            minpdt = min(num, minpdt * num)
            currMax = max(currMax, maxpdt)
        return currMax