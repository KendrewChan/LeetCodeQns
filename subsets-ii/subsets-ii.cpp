class Solution {
    vector<vector<int>> v;
    
    void helper(vector<int>& nums, int start, vector<int> curr) {
        if (find(v.begin(), v.end(), curr) == v.end()) v.push_back(curr);
        for (int i = start; i < nums.size(); i++) {
            curr.push_back(nums[i]);
            helper(nums, i+1, curr);
            curr.pop_back();
        }
    }
    
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> vect;
        helper(nums, 0, vect);
        return v;
    }
};