class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        d = {}
        left, longest = 0, 0
        for i in range(len(s)):
            c = s[i]
            if c in d:
                left = max(left, d[c]+1)
            d[c] = i
            
            longest = max(longest, i-left+1)
        return longest
        
"""
"abcabcbb"
"bbbbb"
"pwwkew"
"abba"
"""