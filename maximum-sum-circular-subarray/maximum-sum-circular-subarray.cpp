class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        // https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
        // Not circular: Normal max subarray
        // Circular: Sum - min subarray
        int sum = nums[0];
        
        int maxSub = nums[0];
        int minSub = nums[0];
        
        int currMax = nums[0];
        int currMin = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int curr = nums[i];
            sum += curr;
            
            currMax = max(curr, curr + currMax);
            currMin = min(curr, curr + currMin);
            
            maxSub = max(maxSub, currMax);        
            minSub = min(minSub, currMin);
        }
        if (sum - minSub == 0) return maxSub;
        return max(maxSub, sum - minSub);
    }
};
/*
[1,-2,3,-2]
[5,-3,5]
[3,-1,2,-1]
[3,-2,2,-3]
[-2,-3,-1]
[-2,4,4,4,6]
[5,5,0,-5,3,-3,2]
[1,-2,3,-2]
*/