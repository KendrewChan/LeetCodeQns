class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = defaultdict()
        d[0] = -1
        maxlen = count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in d:
                maxlen = max(maxlen, i-d[count])
            else:
                d[count] = i 
                # This records the last point which we had a similar imbalance
                # Later on, if we ever have the same imbalance again, minus them off and u get the contiguous length (Note how this is contiguous!)
        return maxlen
        