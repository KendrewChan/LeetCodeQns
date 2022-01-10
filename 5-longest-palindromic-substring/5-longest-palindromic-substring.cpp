class Solution {
public:
    string longestPalindrome(string s) {
        pair<string, int> longest;
        for (int i = 0; i < s.size(); i++) {
            string currOdd = getLongestPalindrome(s, i, i);
            int oddSize = currOdd.size();

            string currEven = i > 0 ? getLongestPalindrome(s, i-1, i) : "";
            int evenSize = currEven.size();
            
            if (oddSize > evenSize && oddSize > longest.second) {
                longest.first = currOdd;
                longest.second = oddSize;
            } else if (evenSize >= oddSize && evenSize > longest.second) {
                longest.first = currEven;
                longest.second = evenSize;
            }
        }
        return longest.first;
    }
    
    string getLongestPalindrome(string s, int left, int right) {
        // Compare left against right
        while (s[left] == s[right]) {
            if (left > 0 && right < s.size()) {
                left--;
                right++;
            } else {
                return s.substr(left, right-left+1);
            }
        }
        return s.substr(left+1, right-left-1);
    }
};