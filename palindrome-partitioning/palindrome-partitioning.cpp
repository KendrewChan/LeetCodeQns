class Solution {
    vector<vector<string>> vect;
    int size;
    
public:
    vector<vector<string>> partition(string s) {
        vector<string> start;
        size = s.size();
        helper(s, 0, start);
        return vect;
    }
    
    void helper(string s, int start, vector<string> curr) {
        if (start == size) vect.push_back(curr);
        else {
            for (int end = start; end < size; end++) {
                if (!isPalindrome(s, start, end)) continue;
                curr.push_back(s.substr(start, end-start+1));
                helper(s, end+1, curr);
                curr.pop_back();
            }
        }
    }
    
    bool isPalindrome(string s, int l, int r) {
        while (l < r) {
            if (s[l++] != s[r--]) return false;
        }
        return true;
    }
};