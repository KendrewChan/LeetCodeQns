class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1,n):
            if i == 1:
                dp[1] = 2
                continue
            dp[i] += dp[i-2] + dp[i-1]
        return dp[n-1]