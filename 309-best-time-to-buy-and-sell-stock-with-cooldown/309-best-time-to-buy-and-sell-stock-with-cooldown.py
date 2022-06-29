class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = -math.inf
        rest = 0
        for price in prices:
            buy, sell, rest = max(buy,rest-price), buy+price, max(rest, sell)
        return max(sell,rest)