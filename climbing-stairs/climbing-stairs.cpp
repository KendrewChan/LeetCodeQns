class Solution {
    map<int, int> hmap;
public:
    int climbStairs(int n) {
        if (n <= 0) return 0;
        if (n <= 2) return n;
        if (hmap[n]) return hmap[n];
        int steps =  climbStairs(n-1) + climbStairs(n-2);
        hmap[n] = steps;
        return steps;
    }
};