class Solution {
public:
    int numTeams(vector<int>& rating) {
        vector<vector<int>> bigger; // Number of elements on rightside greater than current element
        vector<vector<int>> smaller; // Number of elements on rightside lesser than current element
        for (int i = 0; i < rating.size(); i++) {
            int curr = rating[i];
            vector<int> bCount;
            vector<int> sCount;
            for (int j = i+1; j < rating.size(); j++) {
                int next = rating[j];
                if (next > curr) {
                    bCount.push_back(j);
                }
                if (next < curr) {
                    sCount.push_back(j);
                }
            }
            bigger.push_back(bCount);
            smaller.push_back(sCount);
        }
        
        int tCount = 0;
        for (int i = 0; i < rating.size(); i++) {
            vector<int> bCount = bigger[i];
            vector<int> sCount = smaller[i];
            for (int j = 0; j < bCount.size(); j++) {
                int c = bCount[j]; // 2nd number index
                tCount += bigger[c].size(); // Increment by count that's greater than 2nd
            }
            
            for (int j = 0; j < sCount.size(); j++) {
                int c = sCount[j]; // 2nd number index
                tCount += smaller[c].size(); // Increment by count that's less than 2nd
            }
        }
        return tCount;
    }
};