class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        vector<int> valuei;
        vector<int> valuej;
        for (int i = 0; i < values.size(); i++) {
            valuei.push_back(values[i] + i);
            valuej.push_back(values[i] - i);
        }
        
        int maxScore = 0;
        int currLargesti = 0;
        for (int i = 0; i < (values.size()-1); i++) {
            currLargesti = max(currLargesti, valuei[i]);
            int valj = valuej[i+1];
            int score = currLargesti + valj;
            maxScore = max(maxScore, score);
        }
        return maxScore;
    }
};