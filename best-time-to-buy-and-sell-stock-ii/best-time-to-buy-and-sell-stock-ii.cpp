class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Buy low, sell high
        int currProfit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] > prices[i-1]) currProfit += prices[i] - prices[i-1];
        }
        return currProfit;
    }
};