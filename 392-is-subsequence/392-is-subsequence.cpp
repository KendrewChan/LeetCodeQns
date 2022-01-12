class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        for (auto c : t) {
            if (s[i] == c) i++;
            if (i == s.length()) break;
        }
        return i==s.length();
    }
};
