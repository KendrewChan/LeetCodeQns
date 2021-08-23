class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int left = 1;
        int right = nums.size()-1;
        while (left < right) {
            int mid = (left + (right - left) / 2);
            int count = 0; 
            // Number greater than mid
            for (int num : nums) {
                if (num <= mid) count++;
            }
            // E.g. we counted 3 elements, when there's supposed to only be 2 elements up to mid
            if (count <= mid) {
                left = mid+1; // Duplicate on rightside
            } else {
                right = mid;
            }
        }
        
        return left;
    }
};