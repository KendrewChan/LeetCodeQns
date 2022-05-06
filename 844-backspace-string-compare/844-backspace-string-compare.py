class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.backspace(s) == self.backspace(t)
        
    def backspace(self, text):
        curr = ""
        skip = 0
        for c in text[::-1]:
            if c == "#":
                skip += 1
            elif skip > 0:
                skip -= 1
                continue
            else:
                curr = c + curr
        return curr