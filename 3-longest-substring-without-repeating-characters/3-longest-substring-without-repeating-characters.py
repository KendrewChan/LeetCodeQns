class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = right = 0
        max_len = 0
        # Sliding window
        for i in range(len(s)):
            c = s[i]
            if c in d:
                # Move sliding window leftwards
                temp = d[c]+1
                # Remove all values in sliding window up repeated character
                for j in range(left, d[c]+1):
                    c2 = s[j]
                    del d[c2]
                left = temp
            d[c] = i
            right += 1
            max_len = max(max_len, right-left)
        return max_len
            