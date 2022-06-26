class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        maxInc1 = self.getMaxInc(nums1, nums2)
        maxInc2 = self.getMaxInc(nums2, nums1)
        
        return max(sum(nums1)+maxInc1, sum(nums2)+maxInc2)
    
    def getMaxInc(self, nums1, nums2):
        n = len(nums1)
        maxInc = 0
        curr_increment = 0
        for i in range(n):
            n1, n2 = nums1[i], nums2[i]
            curr_increment = max(0,curr_increment+n2-n1)
            maxInc = max(maxInc, curr_increment)
        return maxInc

