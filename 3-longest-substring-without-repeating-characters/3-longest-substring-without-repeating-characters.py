class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = 0
        max_len = 0
        for i in range(len(s)):
            c = s[i]
            if c in d:
                # Left will always be the largest 
                # esp if u find a 2nd repeated character
                left = max(left, d[c]+1)
            d[c] = i
            max_len = max(max_len, i-left+1)
        return max_len
            