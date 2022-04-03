class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        for num in nums:
            val = val ^ num # XOR of itself is zero
        return val