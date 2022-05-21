class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            max_useable_height = min(height[left], height[right])
            width = right-left
            max_area = max(max_area, max_useable_height*width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
            