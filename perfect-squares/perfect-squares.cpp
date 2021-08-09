class Solution {
public:
    int numSquares(int n) {
        if (n <= 0) return 0;
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j*j <= i; j++) {
                // `i-j*j` represents the leftover amt required, the `+1` represents the current j*j
                dp[i] = min(dp[i], 1 + dp[i-j*j]);
            }
        }
        
        return dp[n];
        
    }
};