class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        phrase = ""
        for c in s:
            c = c.lower()
            if c.isalnum():
                phrase += c
        
        for i in range(len(phrase)/2):
            if phrase[i] != phrase[-i-1]:
                return False
        return True