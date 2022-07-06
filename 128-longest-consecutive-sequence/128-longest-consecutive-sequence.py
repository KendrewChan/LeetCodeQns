class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if (num-1) in s:
                continue
            # Pick the starting value
            curr = num
            while (curr+1) in s:
                curr += 1
            # (curr-num+1) just calculates the number of increments from starting point
            longest = max(longest, curr-num+1) 
        return longest
            