class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target-num) in d:
                return [i, d[target-num]]
            d[num] = i
            
        
            