class Solution {
    map<pair<int, int>, int> dp;
    
public:
    int longestPalindromeSubseq(string s) {
        return helper(s, 0, s.size()-1); // Directly start from the longest
    }
    
    int helper(string& s, int l, int r) {
        pair<int, int> key{l, r};
        if (dp[key]) return dp[key];
        if (l == r) return 1;
        if (l > r) return 0;
        int res;
        if (s[l] == s[r]) res = 2 + helper(s, l+1, r-1); 
        // Check both ends
        else res = max(helper(s, l+1, r), helper(s, l, r-1)); 
        // Get max from deleting either left or right element
        dp[key] = res;
        return res;
    }
};