class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        d[")"] = "("
        d["]"] = "["
        d["}"] = "{"
        stk = []
        for c in s:
            if c not in d:
                stk.append(c)
            else:
                if not len(stk):
                    return False
                peek = stk.pop()
                if peek != d[c]:
                    return False
        return not len(stk)