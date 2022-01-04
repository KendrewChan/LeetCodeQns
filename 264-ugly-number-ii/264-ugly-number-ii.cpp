class Solution {
public:
    int nthUglyNumber(int n) {
        int i2 = 0, i3 = 0, i5 = 0;
        vector<int> res{1};
        for (int i = 2; i <= n; i++) {
            int new2 = 2 * res[i2];
            int new3 = 3 * res[i3];
            int new5 = 5 * res[i5];
            int curr = min(new2, min(new3, new5));
            res.push_back(curr);
            if (curr == new2) i2++;
            if (curr == new3) i3++;
            if (curr == new5) i5++;
        }
        return res[n-1];
    }
};