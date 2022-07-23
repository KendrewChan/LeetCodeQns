class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Cant do greedy approach here
        # Lets try dp approach, similar to knapsack problem?
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount):
            for coin in coins:
                nxt = i + coin
                if nxt > amount:
                    continue
                dp[nxt] = min(dp[nxt], dp[i]+1)
        if dp[-1] == math.inf:
            return -1
        return dp[-1]