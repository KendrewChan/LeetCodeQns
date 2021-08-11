class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int smallest = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            int currProfit = prices[i] - smallest;
            maxProfit = max(maxProfit, currProfit);
            smallest = min(smallest, prices[i]);
        }
        return maxProfit;
    }
};