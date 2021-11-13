class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        // Sort into point array, now it becomes like house robbers qns
        int largestSize = 10001;
        vector<int> pointArray(largestSize, 0);
        for (int num : nums) pointArray[num] += num;
        
        pointArray[2] = max(pointArray[2], pointArray[1]);
        for (int i = 3; i < largestSize; i++) {
            pointArray[i] = max(pointArray[i-1], pointArray[i] + pointArray[i-2]);
        }
        return pointArray[largestSize-1];
    }
};
/*
[3,4,2]
[2,2,3,3,3,4]
[4,10,10,8,1,4,10,9,7,6]
*/