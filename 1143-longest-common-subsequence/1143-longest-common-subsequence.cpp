class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        // https://leetcode.com/problems/longest-common-subsequence/discuss/348884/C%2B%2B-with-picture-O(nm)
        int n1 = text1.size(), n2 = text2.size();
        vector<vector<int>> m(n1 + 1, vector<int>(n2 + 1));
        // Do this to avoid [i-1][j-1] checks
        for (int i = 1; i <= n1; i++) {
            for (int j = 1; j <= n2; j++) {
                  if (text1[i - 1] == text2[j - 1]) {
                      m[i][j] = m[i - 1][j - 1] + 1;
                      // Add on from prevs
                  } else {
                      m[i][j] = max(m[i - 1][j], m[i][j - 1]);
                      // Maintain max
                  }
            }
        }
        return m[n1][n2];
    }
};