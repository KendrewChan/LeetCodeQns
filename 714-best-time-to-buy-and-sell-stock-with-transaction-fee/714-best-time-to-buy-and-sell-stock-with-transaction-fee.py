class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -math.inf
        hold = 0
        for price in prices:
            buy, hold = max(buy,hold-price),max(hold,buy+price-fee)
        return hold