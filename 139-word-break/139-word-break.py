class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        visited = []
        curr = [0]
        while len(curr) > 0:
            start = curr.pop(0)
            if start in visited:
                continue
            visited.append(start)
            for end in range(start+1, len(s)+1): # Check by index instead of by word
                if s[start:end] in wordDict:
                    if end == len(s):
                        return True
                    curr.append(end)
        return False
                        
"""
"leetcode"
["leet","code"]
"applepenapple"
["apple","pen"]
"catsandog"
["cats","dog","sand","and","cat"]
"aaaaaaa"
["aaaa","aaa"]
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""
                