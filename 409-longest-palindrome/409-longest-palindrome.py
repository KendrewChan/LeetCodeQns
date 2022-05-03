class Solution(object):    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {}
        for c in s:
            if c not in hmap:
                hmap[c] = 0
            hmap[c] += 1
        
        hasOdd = False
        longest = 0
        for key in hmap:
            value = hmap[key]
            if value % 2 == 0:
                longest += value
            else:
                hasOdd = True
                longest += value-1
        return longest+1 if hasOdd else longest