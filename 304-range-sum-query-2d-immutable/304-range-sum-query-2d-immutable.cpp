class NumMatrix {
public:
    int sizeX, sizeY;
    vector<vector<int>> sum;
    int extractSum(int i, int j) {
        if (i < 0 || j < 0) return 0;
        if (i >= sizeX) i = sizeX - 1;
        if (j >= sizeY) j = sizeY - 1;
        return sum[i][j];
    }
    
    NumMatrix(vector<vector<int>>& mat) {
        // Similar solution to `https://leetcode.com/problems/matrix-block-sum/`
        sizeX = mat.size();
        sizeY = mat[0].size();
        
        vector<vector<int>> temp(sizeX, vector<int>(sizeY, 0));
        sum = temp;
        // Calculate prefix matrix 
        for (int i = 0; i < sizeX; i++) {
            for (int j = 0; j < sizeY; j++) {
                sum[i][j] = mat[i][j] + extractSum(i-1, j) + extractSum(i, j-1) - extractSum(i-1, j-1);
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return extractSum(row2, col2) - extractSum(row1-1, col2) - extractSum(row2, col1-1) + extractSum(row1-1, col1-1);
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */