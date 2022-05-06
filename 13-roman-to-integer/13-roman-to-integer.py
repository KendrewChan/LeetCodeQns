class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = hmap[s[-1]] # Set last value as initial
        for i in range(len(s)-2,-1,-1):
            curr = s[i]
            prev = s[i+1]
            if hmap[curr] < hmap[prev]:
                total -= hmap[curr]
            else:
                total += hmap[curr]
        return total
                
            