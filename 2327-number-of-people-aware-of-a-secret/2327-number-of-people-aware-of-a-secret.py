class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = pow(10,9)+7
        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            prevDelay, prevForget = i-delay, i-forget
            dp[i]=dp[i-1]
            if prevForget >= 0:
                toRemove = dp[prevForget]
                for j in range(prevForget,i+1):
                    if not dp[j]:
                        break
                    dp[j] -= toRemove
            if prevDelay >= 0:
                dp[i] += dp[prevDelay] 
            dp[i] = dp[i] % mod
        return dp[-1]
    
"""
Ans: 5,6,2
6
2
4
4
1
3
6
1
2
"""