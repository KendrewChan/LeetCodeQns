class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxPdt = -99;
        int currMax = 1;
        int currMin = 1;
        for (int num : nums) {
            if (num < 0) swap(currMax, currMin);

            currMax = max(num, num * currMax);
            currMin = min(num, num * currMin);
            
            maxPdt = max(maxPdt, currMax);
        }
        return maxPdt;
    }
};
/*
[2,3,-2,4]
[-2,0,-1]
[-2,3,-4]
*/