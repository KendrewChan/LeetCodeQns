class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [1]
        for i in range(rowIndex):
            temp = [1]
            for j in range(1, len(dp)):
                temp.append(dp[j-1] + dp[j])
            temp.append(1)
            dp = temp
        return dp