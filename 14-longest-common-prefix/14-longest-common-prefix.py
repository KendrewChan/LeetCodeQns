class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        idx = 0
        while idx < len(strs[0]):
            c = strs[0][idx]
            for s in strs:
                if idx >= len(s) or c != s[idx]:
                    return s[:idx]
            idx += 1
            
        return strs[0][:idx]
                