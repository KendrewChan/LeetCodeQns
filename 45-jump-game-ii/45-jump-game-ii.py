class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            reachable = nums[i]+i
            for j in range(i+1, reachable+1):
                if j >= len(nums):
                    break
                dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]