class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        nums[1] = max(nums[0], nums[1]);
        int size = nums.size();
        for (int i = 2; i < size; i++) {
            nums[i] = max(nums[i] + nums[i-2], nums[i-1]); // Either add-on or maintain
        }
        return nums[size-1];
    }
};
/*
[1]
[2,1]
[1,2,3,1]
[2,1,1,2]
[2,7,9,3,1]
*/