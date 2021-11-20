class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() <= 2) return 0;
        int numSlices = 0;
        int currSize = 2;
        int prevDiff = nums[1] - nums[0];
        for (int i = 2; i < nums.size(); i++) {
            int diff = nums[i] - nums[i-1];
            if (prevDiff == diff) currSize++;
            else {
                prevDiff = diff;
                i++;
                int nextDiff = nums[i] - nums[i-1];
                if (nextDiff == prevDiff) currSize = 3;
                else currSize = 2;
                prevDiff = nextDiff;
            }
            if (currSize >= 3) numSlices += currSize - 2;
        }
        return numSlices;
    }
};
/*
[1,2,3,4]
[1]
[7,7,7,7]
[3,-1,-5,-9]
[7,7,7,7,3,-1,-5,-9]
*/