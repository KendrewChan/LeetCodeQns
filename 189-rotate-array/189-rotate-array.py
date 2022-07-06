class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotates = k%n
        res = nums[n-rotates:] + nums[:n-rotates]
        for i in range(n):
            nums[i] = res[i]