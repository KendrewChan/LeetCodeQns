class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            int curr = nums[i];
            for (int j = i+1; j < nums.size(); j++) {
                if (!curr) {
                    if (!nums[j]) continue;
                    nums[i] = nums[j];
                    nums[j] = 0;
                    break;
                }
            }
        }
    }
};