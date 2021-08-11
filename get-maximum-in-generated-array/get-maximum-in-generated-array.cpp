class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n <= 1) return n;
        vector<int> dp;
        dp.push_back(0);
        dp.push_back(1);
        int m = 1;
        for (int i = 2; i <= n; i++) {
            int val;
            if (i % 2 == 0) val = dp[i/2];
            else val = dp[(i-1)/2] + dp[(i-1)/2 + 1];
            dp.push_back(val);
            m = max(m, val);
        }
        return m;
    }
};