class TrieNode:
    def __init__(self, val, isWord):
        self.children = {}
        self.val = val
        self.isWord = isWord

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None, False)

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c, False)
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = [self.root]
        for c in word:
            temp = []
            while len(curr):
                node = curr.pop()
                if c == '.':
                    temp += node.children.values()
                    continue
                if not len(node.children):
                    continue
                if c in node.children:
                    temp.append(node.children[c])
            if not len(temp):
                return False
            curr = temp
        res = False
        for node in curr:
            if node.isWord:
                return True
        return False
            
"""
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b..d"]]

"""
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)