class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxi = max(nums)
        freqArr = [0 for _ in range(maxi+1)]
        for num in nums:
            freqArr[num] += 1
            
        for i in range(2,maxi+1):
            freqArr[i] = max(freqArr[i-1], freqArr[i]*i+freqArr[i-2])
        
        return freqArr[-1]