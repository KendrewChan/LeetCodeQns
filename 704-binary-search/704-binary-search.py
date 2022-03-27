class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1

        while low < high:
            mid = low + int((high-low+1)/2)
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid
        return low if nums[low] == target else -1
    
        # while low < high:
        #         mid = low + int((high-low)/2)
        #         if nums[mid] >= target:
        #             high = mid
        #         else:
        #             low = mid+1
        #     return high if nums[low] == target else -1