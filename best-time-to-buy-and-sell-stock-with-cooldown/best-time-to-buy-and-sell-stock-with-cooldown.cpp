class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
        int sold = 0; 
        int buy = INT_MIN;
        int rest = 0;
        for (int price : prices) {
            int prevSold = sold;
            sold = buy + price; // Price if you sell now
            buy = max(buy, rest - price); // Always hold the smallest priced
            rest = max(rest, prevSold); // Hold the highest profit
        }
        return max(sold, rest);
    }
};