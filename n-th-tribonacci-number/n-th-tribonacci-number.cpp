class Solution {
    map<int, int> hmap;
    
public:
    int tribonacci(int n) {
        if (n <= 1) return n;
        if (n == 2) return 1;
        if (hmap.count(n)) {
            return hmap[n];
        } else {
            int t =  tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
            hmap[n] = t;
            return t;
        }
    }
};