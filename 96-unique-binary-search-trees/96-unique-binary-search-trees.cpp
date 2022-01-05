class Solution {
    map<int, int> dp{{0, 1}, {1, 1}};
    
public:
    int numTrees(int n) {
        // https://leetcode.com/problems/unique-binary-search-trees/discuss/1565543/C%2B%2BPython-5-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Catalan-O(N)
        if (dp.count(n)) return dp[n];
        int res = 0;
        for (int i = 1; i <= n; i++) {
            res += numTrees(i-1) * numTrees(n-i);
        }
        return dp[n] = res;
    }
};