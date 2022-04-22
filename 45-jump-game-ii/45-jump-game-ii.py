class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[0] = 0
        for i in range(n):
            if dp[i] < 0:
                continue
            toLoop = i+nums[i]+1
            endLoop = n if toLoop > n else toLoop
            for j in range(i+1, endLoop):
                if dp[j] == -1:
                    dp[j] = dp[i]+1
                    continue
                dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]