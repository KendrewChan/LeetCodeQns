class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        wordDict.sort(key=lambda x: -len(x))
        dp = [False for _ in s]
        curr = [0]
        while len(curr) > 0:
            temp = []
            for i in curr:
                c = s[i]
                for word in wordDict:
                    if word[0] != c:
                        continue
                    nxt = i+len(word)
                    if nxt > len(s) or dp[nxt-1]:
                        continue
                    if s[i:nxt] != word:
                        continue
                    dp[nxt-1] = True
                    temp.append(nxt)
                    if nxt == len(s):
                        return True
            curr = temp
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
                