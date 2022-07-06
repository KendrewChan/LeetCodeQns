class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotates = k%n
        nums[:] = nums[n-rotates:] + nums[:n-rotates]