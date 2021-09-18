class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int l = p.size();
        vector<int> toCompare(26,0);
        for (auto c : p) toCompare[c-'a']++;
        vector<int> freqArr(26, 0);
        vector<int> ans;
        for (int i = 0; i < s.size(); i++) {
            int c = s[i] - 'a';
            freqArr[c]++;
            if (i >= l) {
                int prev = s[i-l]-'a';
                freqArr[prev]--;
            }
            bool same = true;
            for (int j = 0; j < 26; j++) {
                if (toCompare[j] != freqArr[j]) {
                    same = false;
                    break;
                }
            }
            if (same) ans.push_back(i-l+1);
        }
        return ans;
    }
};