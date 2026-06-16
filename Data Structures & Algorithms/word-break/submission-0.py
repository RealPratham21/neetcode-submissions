from functools import lru_cache

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()

            curr = curr.children[w]
        
        curr.isEnd = True
    
    def search(self, word):
        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
            
            curr = curr.children[w]
        
        return curr.isEnd

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tree = Trie()
        n = len(s)

        for word in wordDict:
            tree.insert(word)

        @lru_cache(None)
        def dp(pos):
            if pos >= n:
                return True
            
            res = False

            for i in range(pos, n):
                if tree.search(s[pos:i+1]):
                    res |= dp(i + 1)
            
            return res
        
        return dp(0)