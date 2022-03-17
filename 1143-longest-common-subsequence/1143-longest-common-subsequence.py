class Solution(object):
    def __init__(self):
        self.d = {}
    
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        return self.memoize(text1,text2,len(text1)-1, len(text2)-1)
        
            
    def memoize(self, text1, text2, i1, i2):
        if (i1 < 0 or i2 < 0):
            return 0
        elif ((i1, i2) in self.d):
            return self.d[(i1, i2)]
        else:
            res = 0
            if (text1[i1] == text2[i2]):
                res = 1 + self.memoize(text1,text2,i1-1,i2-1)
            else:
                sub1 = self.memoize(text1,text2,i1-1,i2)
                sub2 = self.memoize(text1,text2,i1,i2-1)
                res = max(sub1, sub2)
                
            self.d[(i1, i2)] = res
            return res