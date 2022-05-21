class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Cant do greedy approach here
        # Lets try dp approach, similar to knapsack problem?
        overlimit = pow(10,4)+1
        dp = [overlimit for _ in range(amount+1)]
        dp[0] = 0
        
        for i in range(amount):
            curr = dp[i]
            for coin in coins:
                nxt = i+coin
                if nxt > amount:
                    continue
                dp[nxt] = min(dp[nxt], curr+1)
        if dp[-1] == overlimit:
            return -1
        return dp[-1]
        