class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> dp;
        for (int i = 0; i <= rowIndex; i++) {
            vector<int> vect;
            for (int j = 0; j < i + 1; j++) {
                if (j == 0 || j == i) vect.push_back(1);
                else vect.push_back(dp[j-1] + dp[j]);
            }
            dp = vect;
        }
        return dp;
    }
};