class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()

            curr = curr.children[w]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
        
            curr = curr.children[w]

        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for w in prefix:
            if w not in curr.children:
                return False

            curr = curr.children[w]
        
        return True
        