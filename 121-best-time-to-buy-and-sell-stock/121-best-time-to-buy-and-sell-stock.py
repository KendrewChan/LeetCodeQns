class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        curr = prices[0]
        for price in prices:
            curr = min(curr, price)
            maxprofit = max(maxprofit, price-curr)
        return maxprofit
            
            