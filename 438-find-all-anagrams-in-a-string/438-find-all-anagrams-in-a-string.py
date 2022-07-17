class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Sliding window with freq array
        required = [0 for _ in range(26)]
        curr_d = [0 for _ in range(26)]
        for c in p:
            required[self.charToInt(c)] += 1
        res = []
        curr = []
        for i in range(len(s)):
            c = s[i]
            if len(curr) == len(p):
                popped = curr.pop(0)
                curr_d[self.charToInt(popped)] -= 1
    
            curr.append(c)
            curr_d[self.charToInt(c)] += 1
    
            if len(curr) != len(p):
                continue
                
            if required == curr_d:
                res.append(i-len(p)+1)
        return res
    
    def charToInt(self, c):
        return ord(c)-ord('a')
                    
                    