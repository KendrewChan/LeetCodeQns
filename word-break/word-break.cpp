class Solution {
public:
    bool wordBreak(string s, vector<string>& d) {
        vector<bool> dp(s.size(), false);
        dp[0] = true;
        
        for (int i = 0; i < s.size(); i++) {
            if (!dp[i]) continue;
            for (int j = i+1; j <= s.size(); j++) {
                string substr = s.substr(i, j-i);
                if (find(d.begin(), d.end(), substr) != d.end()) {
                    dp[j] = true;
                    // cout << i << " : " << j << " -> " << substr << endl;
                }
            }
        }
        return dp[s.size()];
    }
};