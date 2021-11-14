class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        int size = nums.size();
        vector<int> hops(size, 0);
        for (int i = 0; i < size; i++) {
            cout << hops[i] << endl;
            int hoppable = i + nums[i];
            if (hoppable+1 >= size) return hops[i]+1;
            for (int j = i+1; j <= hoppable; j++) {
                if (!hops[j]) hops[j] = hops[i]+1;
                else hops[j] = min(hops[j], hops[i]+1);
            }
        }
        return 0;
    }
};
/*
[0]
[1]
[2,3,1,1,4]
[2,3,0,1,4]
[1,1,1,1,1]
[1,2,1,1,1]
*/