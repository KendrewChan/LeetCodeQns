class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = nums[0];
        int sum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int num = nums[i];
            sum = max(num, sum + num);
            maxSub = max(sum, maxSub);
        }
        return maxSub;
    }
};
/*
[-2,1,-3,4,-1,2,1,-5,4]
[1]
[5,4,-1,7,8]
*/