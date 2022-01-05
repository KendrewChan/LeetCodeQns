class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> dp{1};
        for (int i = 1; i <= rowIndex; i++) {
            vector<int> vect{1};
            for (int j = 1; j < i; j++) {
                vect.push_back(dp[j-1] + dp[j]);
            }
            vect.push_back(1);
            dp = vect;
        }
        return dp;
    }
};