class Solution {
public:
    int trap(vector<int>& height) {
        int maxHeight = 0;
        for (int h : height) maxHeight = max(maxHeight, h);
        
        int rain = 0;
        int left = 0;
        int leftBound = 0;
        for (int i = 0; i < height.size(); i++) {
            int h = height[i];
            if (h == maxHeight) {
                leftBound = i;
                break;
            }
            if (h < left) rain += left-h;
            else left = h;
        }
        
        int right = 0;
        int rightBound = 0;
        for (int i = height.size()-1; i >= 0; i--) {
            int h = height[i];
            if (h == maxHeight) {
                rightBound = i;
                break;
            }
            if (h < right) rain += right-h;
            else right = h;
        }
        
        // Check middle
        for (int i = leftBound+1; i < rightBound; i++) {
            rain += maxHeight - height[i];
        }
        return rain;
    }
};
/*
[0,1,0,2,1,0,1,3,2,1,2,1]
[4,2,0,3,2,5]
[2,0,2]
*/