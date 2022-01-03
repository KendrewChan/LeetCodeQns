class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) return 0;
        int num = 0;
        int count = 2;
        int diff = nums[1] - nums[0];
        for (int i = 2; i < nums.size(); i++) {
            int d = nums[i] - nums[i-1];
            if (d != diff) {
                diff = d;
                count = 2;
            } else {
                count++;
                if (count < 3) continue;
                if (count == 3) num++;
                if (count > 3) num += count-2;
            }
        }
        return num;
    }
};
/*
[1,2,3,4]
[1]
[7,7,7,7]
[3,-1,-5,-9]
[7,7,7,7,3,-1,-5,-9]
*/