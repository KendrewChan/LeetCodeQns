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
        for c in text:
            if c == "#":
                curr = curr[:-1]
            else:
                curr += c
        return curr