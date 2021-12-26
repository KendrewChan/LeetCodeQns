class Solution {
    
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        int size = nums1.size();
        map<int, int> first;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                int curr = nums1[i]+nums2[j];
                first[curr]++;
            }
        }
        int count = 0;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                int curr = nums3[i]+nums4[j];
                count += first[-curr];
            }
        }
        return count;
    }
};