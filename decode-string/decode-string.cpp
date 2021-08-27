class Solution {
public:
    string decodeString(string s) {
        vector<int> numOpen; // Represents number of open as well as each multiplier
        string ans = "";
        vector<string> strOpen;
        string numStr = "";
        string stray = "";
        for (auto c : s) {
            if (c == '[') {
                numOpen.push_back(atoi( numStr.c_str()));
                strOpen.push_back("");
                numStr = "";
            } else if (c == ']') {
                string curr = strOpen.back();
                string temp2 = "";
                for (int i = 0; i < numOpen.back(); i++) temp2 += curr;
                strOpen.pop_back();
                numOpen.pop_back();
                if (numOpen.empty()) {
                    ans += temp2;
                } else {
                    strOpen.back() += temp2;
                }
            } else if (c >= '0' && c <= '9') {
                numStr += c;
                ans += stray;
                stray = "";
            } else if (!strOpen.empty()) {
                strOpen.back() += c;
            } else {
                stray += c;
            }
        }
        
        return ans + stray;
    }
};
/*
"3[a]2[bc]"
"2[abc]3[cd]ef"
"abc3[cd]xyz"
"3[a2[c]]"
*/