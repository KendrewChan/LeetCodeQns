class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bitcount = 0
        while n:
            n = n&(n-1) # AND operator on n and (n-1) flips the least significant 1-bit of n to 0
            bitcount += 1
        return bitcount