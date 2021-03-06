class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for (int i = triangle.size()-1; i >= 1; i--) {
            for (int j = i; j >= 1; j--) {
                triangle[i-1][j-1] += min(triangle[i][j], triangle[i][j-1]);
            }
        }
        return triangle[0][0];
    }
};