class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/longest-repeating-character-replacement/discuss/765776/Python%3A-Two-Pointers-%2B-Process-for-coding-interviews
        l = 0
        c_freq = {}
        longest = 0
        for r in range(len(s)):
            r_char = s[r]
            if r_char not in c_freq:
                c_freq[r_char] = 0
            c_freq[r_char] += 1
            
            # Replacements cost = cells count between left and right - highest frequency
            cells_count, curr_max = r - l + 1, max(c_freq.values())
            
            if (cells_count - curr_max) <= k: # if can be replaced by k
                longest = max(longest, cells_count)
            else: # if can't be replaced by k, we move left pointer
                l_char = s[l]
                c_freq[l_char] -= 1
                if c_freq[l_char] == 0:
                    del c_freq[l_char]
                l += 1
        return longest
            