class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int maxLen = 0, currLen = 0, currNegs = 0, firstNegIdx = 0;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (num == 0) {
                currNegs = 0;
                currLen = 0;
                continue;
            } 
            currLen++;
            if (num < 0) {
                currNegs++;
                if (currNegs == 1) firstNegIdx = i; 
            }
            // firstNegIdx is the tie breaker. 
            // E.g. [0,1,-2,-3,-4] , firstNegIdx = -2, 
            // later we can compare "currLen" -> [1,-2,-3] against "i - firstNegIdx" -> [-3,-4]
            maxLen = max(maxLen, currNegs % 2 == 0 ? currLen : i - firstNegIdx);
        }
        return maxLen;
    }
};
/*
[1,-2,-3,4]
[0,1,-2,-3,-4]
[-1,-2,-3,0,1]
[-1,2]
[1,2,3,5,-6,4,0,10]
*/