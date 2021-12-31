class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int maxScore = 0;
        int currMax = values[0] + 0;
        for (int i = 1; i < values.size(); i++) {
            int iVal = values[i] + i;
            int jVal = values[i] - i;
            
            maxScore = max(maxScore, currMax + jVal);
            currMax = max(currMax, iVal);
        }
        return maxScore;
    }
};