class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            freqArr = [0 for _ in range(26)]
            for c in s:
                freqArr[ord(c)-ord('a')] += 1
            tpl = tuple(freqArr)
            if tpl not in d:
                d[tpl] = []    
            d[tpl].append(s)
        return [d[key] for key in d]