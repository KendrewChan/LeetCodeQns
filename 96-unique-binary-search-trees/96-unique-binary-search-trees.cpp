class Solution {
    map<int, int> dp{{0, 1}, {1, 1}};
    
public:
    int numTrees(int n) {
        if (dp.count(n)) return dp[n];
        int res = 0;
        for (int i = 1; i <= n; i++) {
            res += numTrees(i-1) * numTrees(n-i);
        }
        return dp[n] = res;
    }
};