class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_avail = 0
        for i in range(n):
            if i > max_avail:
                break
            max_avail = max(max_avail, i+nums[i])
        return max_avail >= n-1