class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_size = 1
        dp = [1 for _ in range(len(nums))] # Each element is a subsequence of size 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if (nums[j] < nums[i]): # Only check for those with correct format
                    dp[i] = max(dp[i], dp[j]+1) 
                    # dp[i] represents current max
                    # dp[j]+1 represents a prev subsequence added on with current element
            longest_size = max(longest_size, dp[i])
        return longest_size