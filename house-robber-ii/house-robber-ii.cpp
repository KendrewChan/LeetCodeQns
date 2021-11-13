class Solution {
    int robOriginal(vector<int> nums, int start, int end) {
        nums[start+1] = max(nums[start], nums[start+1]);
        for (int i = start+2; i < end; i++) {
            nums[i] = max(nums[i-1], nums[i] + nums[i-2]);
        }
        return nums[end-1];
    }
    
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);
        return max(
            robOriginal(nums, 0, nums.size()-1),
            robOriginal(nums, 1, nums.size())
        );
    }
};
/*
[2,3,2]
[1,2,3,1]
[1,2,3]
[0,0]
*/