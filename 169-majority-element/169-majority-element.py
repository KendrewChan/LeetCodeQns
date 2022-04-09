class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
        curr = -1
        counter = 0
        for num in nums:
            if counter == 0:
                curr = num
                counter = 1
            elif num == curr:
                counter += 1
            else:
                counter -= 1
        return curr
            