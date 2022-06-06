class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sol = []
        self.helper(nums, [], 0)
        return self.sol
        
    def helper(self, nums, curr, start):
        self.sol.append(curr)
        for i in range(start, len(nums)):
            self.helper(nums, curr + [nums[i]], i+1)