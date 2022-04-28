class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for j in t:
            if j not in d:
                return False
            d[j] -= 1
        for k in d:
            if d[k]:
                return False
        return True