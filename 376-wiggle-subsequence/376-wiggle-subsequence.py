class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Extended Variation of Longest Increasing Subsequence
        # https://leetcode.com/problems/longest-increasing-subsequence/
        longest_size = 1
        dp_positive = [1 for _ in range(len(nums))]
        dp_negative = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[j] < nums[i]): # For increment
                    # Compare current max against previous max + 1
                    # Previous max in this case must be from the decrement array -- dp_negative
                    dp_positive[i] = max(dp_positive[i], dp_negative[j]+1)
                    
                if (nums[j] > nums[i]): # For decrement
                    # Compare current max against previous max + 1
                    # Previous max in this case must be from the increment array -- dp_positive
                    dp_negative[i] = max(dp_negative[i], dp_positive[j]+1)
            longest_size = max(longest_size, max(dp_positive[i], dp_negative[i]))
        return longest_size