class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(n+1):
            if i == 0:
                arr.append(0)
            elif i % 2 == 0:
                arr.append(arr[i//2])
            else:
                arr.append(arr[i//2]+1)
        return arr
            