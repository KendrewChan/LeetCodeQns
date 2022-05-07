class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Since length of n is always 32, we can compare it against a mask
        bitcount = 0
        mask = 1 # Equivalent to 00000000000000000000000000000001
        for i in range(32):
            if (n & mask): # Compare rightmost bit
                bitcount += 1
            mask = mask << 1 # Shift leftwards 1, e.g. mask becomes 00000000000000000000000000000010
        return bitcount