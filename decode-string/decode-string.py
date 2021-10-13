class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        num = "" # integer value
        lst = []
        slst = []
        for i in s:
            if (i.isdigit()):
                num += i
            elif (i == '['):
                lst.append(int(num))
                slst.append("")
                num = ""
            elif (i == ']'):
                last = lst.pop()
                slast = slst.pop()
                curr = slast * last
                if not slst:
                    ans += curr
                else:
                    slst[-1] += curr
            elif slst:
                slst[-1] += i
            else:
                ans += i
        return ans
