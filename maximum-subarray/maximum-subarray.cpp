class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> sum(nums.size(), 0);
        sum[0] = nums[0];
        int sumMax = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int curr = max(nums[i], sum[i-1]+nums[i]);
            sum[i] = curr;
            sumMax = max(sumMax, curr);
        }
        return sumMax;
    }
};
/*
[-2,1,-3,4,-1,2,1,-5,4]
[1]
[5,4,-1,7,8]
*/