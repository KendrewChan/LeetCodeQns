class Solution {
public:
    bool canJump(vector<int>& nums) {
        int furthestIdx = 0;
        for (int i = 0; i < nums.size(); i++) {
            furthestIdx = max(furthestIdx, i + nums[i]);
            if (furthestIdx == i) break;
        }
        return furthestIdx+1 >= nums.size();
    }
};