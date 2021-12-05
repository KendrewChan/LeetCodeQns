class Solution {
    int numWays = 0;
    map<pair<int, int>, int> memo;
    
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        return helper(nums, target, 0, 0);
    }
    
    int helper(vector<int>& nums, int target, int start, int curr) {
        pair<int, int> p{start, curr};
        if (memo.count(p)) return memo[p];
        if (start == nums.size()) {
            if (curr == target) return 1;
            return 0;
        }
        int minus = helper(nums, target, start+1, curr - nums[start]);
        int add = helper(nums, target, start+1, curr + nums[start]);
        int ans = minus + add;
        memo[p] = ans;
        return ans;
    }
};

