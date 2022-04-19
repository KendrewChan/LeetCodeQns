class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = s[-1]
        n = len(s)
        dp = [[0]*n for _ in range(n)] # 2d array, dp[i][j] is True if s[i:j] is a palindrome or not
        #filling out the diagonal by 1
        for i in range(n):
            dp[i][i] = True # Make rightwards diagonal column True
            # longest = s[i] # Idk why this matters and why i can't just set longest = s[-1]
        
        for i in range(n-1,-1,-1): # Start from the back
            for j in range(i+1,n): # Go rightwards
                if s[i] == s[j] and (j-i==1 or dp[i+1][j-1]):
                    # Check if letters match. First loop is always correct. 
                    # Check the leftward diagonal dp[i+1][j=1] see if its correct -> This continues to cascade leftwards depending on length of string. This is the key part of how the DP array knows whether a string is a palindrome or not
                    dp[i][j] = True
                    if len(longest) < len(s[i:j+1]):
                        longest = s[i:j+1]
                
        return longest
                    
        