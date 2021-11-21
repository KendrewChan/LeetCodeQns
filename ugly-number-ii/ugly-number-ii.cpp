class Solution {    
public:
    int nthUglyNumber(int n) {
        if (n <= 0) return false;
        if (n == 1) return true;
        int i2 = 0, i3 = 0, i5 = 0;
        vector<int> k;
        k.push_back(1);
        for (int i = 1; i < n; i++) {
            int m = min(k[i2]*2, min(k[i3]*3, k[i5]*5));
            // Find next min -> increment counter
            if (m == k[i2]*2) i2++;
            if (m == k[i3]*3) i3++;
            if (m == k[i5]*5) i5++;
            k.push_back(m);
        }
        return k[n-1];
    }
};