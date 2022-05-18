class Solution(object):    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.sol = []
        self.helper(nums, [], 0)
        return self.sol
        
        
    def helper(self, nums, curr, start):
        self.sol.append(curr)
        for i in range(start, len(nums)):
            self.helper(nums,curr+[nums[i]],i+1)