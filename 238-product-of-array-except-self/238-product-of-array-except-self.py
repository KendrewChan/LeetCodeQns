class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [num for num in nums]
        for i in range(1,len(prefix)):
            prefix[i] *= prefix[i-1]
        
        curr_suffix = nums[-1]
        for i in range(len(nums)-2,0,-1):
            temp = nums[i]
            nums[i] = prefix[i-1] * curr_suffix
            curr_suffix *= temp
            
        nums[-1] = prefix[-2]
        nums[0] = curr_suffix
        return nums
            