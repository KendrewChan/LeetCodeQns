class Solution {
    vector<vector<bool>> visited;
    
public:
    int numIslands(vector<vector<char>>& grid) {
        // Have a visited array
        // For each (row, column) dfs the entire island and mark as visited
        // Increment count
        // If visited alrdy, skip, if not repeat dfs
        for (int i = 0; i < grid.size(); i++) {
            vector<bool> vect(grid[0].size(), false);
            visited.push_back(vect);
        }
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (!visited[i][j] && grid[i][j] == '1') count++;
                dfs(grid, i, j);
            }
        }
        return count;
    }
    
    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || i > (grid.size()-1) || 
            j < 0 || j > (grid[0].size()-1) ||
            grid[i][j] == '0' || visited[i][j]) return;
        visited[i][j] = true;
        dfs(grid, i-1, j);
        dfs(grid, i+1, j);
        dfs(grid, i, j-1);
        dfs(grid, i, j+1);
    }
};
/*
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
[["1","1","1"],["0","1","0"],["1","1","1"]]
*/