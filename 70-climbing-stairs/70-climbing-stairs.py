class Solution(object):
    memoize = {}
    memoize[1] = 1
    memoize[2] = 2
        
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n in self.memoize:
            return self.memoize[n]
        self.memoize[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memoize[n]