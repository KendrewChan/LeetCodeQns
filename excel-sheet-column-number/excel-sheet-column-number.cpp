class Solution {
public:
    int titleToNumber(string columnTitle) {
        int denom = 0;
        int total = 0;
        for (int i = columnTitle.size()-1; i >= 0; i--) {
            int num = columnTitle[i] - 'A' + 1;
            int p = pow(26, denom);
            total += p * num;
            denom++;
        }
        return total;
    }
};