class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high-low)/2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                high = mid
            else:
                low = mid+1
        return -1