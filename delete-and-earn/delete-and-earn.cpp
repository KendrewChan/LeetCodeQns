class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int maxi = 0;
        for (int i : nums) maxi = max(maxi, i);
        vector<int> freqVect(maxi, 0);
        for (int i : nums) freqVect[i-1]++;
        for (int i = 0; i < freqVect.size(); i++) freqVect[i] *= i+1;
        
        return rob(freqVect);
    }
    
    int rob(vector<int>& nums) {
        // Re-use house robber problem
        int size = nums.size();
        for (int i = 1; i < size; i++) {
            nums[i] = max(nums[i] + (i > 1 ? nums[i-2] : 0), nums[i-1]); // Either add-on or maintain
        }
        return nums[size-1];
    }
};