class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = ""
        for i in range(1, len(s)):
            even = self.isPalindrome(s, i-1,i)
            odd = self.isPalindrome(s, i, i)
            l = self.getLongest(even, odd)
            longest = self.getLongest(longest, l)
        return longest
        
    def getLongest(self, curr: str, toCompare: str) -> str:
        if len(curr) > len(toCompare):
            return curr
        return toCompare
        
    def isPalindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
            