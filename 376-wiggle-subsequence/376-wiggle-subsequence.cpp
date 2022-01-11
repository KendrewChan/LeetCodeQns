class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        // Variation of longest increasing subsequence (albeit abit slow)
        // Longest Increasing Subsequence: https://leetcode.com/problems/longest-increasing-subsequence/
        int n = nums.size();
        vector<int> wiggleDown(n, 1);
        vector<int> wiggleUp(n, 1);
        int longest = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) wiggleUp[i] = max(wiggleUp[i], wiggleDown[j]+1);
                else if (nums[j] > nums[i]) wiggleDown[i] = max(wiggleDown[i], wiggleUp[j]+1);
            }
            int maxWiggle = max(wiggleDown[i], wiggleUp[i]);
            longest = max(longest, maxWiggle);
        }
        return longest;
    }
};