class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s[0] == '0'):
            return 0
        self.n = len(s)
        dp = [-1 for _ in range(self.n+1)] # Last index will not be used
        dp[self.n]=1
        return self.helper(s,0,dp)
    
    def helper(self, s, start, dp):
        if dp[start] > -1: # Since last index is set to 1, we'll return 1 upon reaching last index or when '0' reached
            return dp[start]
        if s[start] == '0':
            dp[start] = 0
            return 0
        # Case 1: Choose single letter
        res = self.helper(s, start+1, dp)
        # Case 2: Choose double letter
        if start < self.n-1 and (s[start] == '1' or (s[start] == '2' and s[start+1] <= '6')):
            res += self.helper(s, start+2, dp)
        dp[start] = res
        return dp[start]
            
            
            
            
        