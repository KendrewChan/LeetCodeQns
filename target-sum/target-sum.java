class Solution { 
    int numWays = 0;
    
    public int findTargetSumWays(int[] nums, int target) {
        helper(nums, target, 0, 0);
        return numWays;
    }
    
    void helper(int[] nums, int target, int start, int curr) {
        if (start == nums.length) {
            if (curr == target) numWays++;
        } else {
            helper(nums, target, start+1, curr - nums[start]);
            helper(nums, target, start+1, curr + nums[start]);
        }
    }
}