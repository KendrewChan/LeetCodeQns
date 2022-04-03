class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(0, len_s/2):
            s[i], s[len_s-i-1] = s[len_s-i-1], s[i]