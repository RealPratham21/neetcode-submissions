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
    
    def find(self, word):
        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
            
            curr = curr.children[w]
        
        return curr.isEnd


    def find_pref(self, word):
        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
            
            curr = curr.children[w]
        
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        
        trie = Trie()

        for word in words:
            trie.insert(word)

        res = set()

        for i in range(m):
            for j in range(n):
                dfs = [(i, j, board[i][j], set())]

                while dfs:
                    x, y, c_word, visited = dfs.pop()

                    if trie.find(c_word):
                        res.add(c_word)
                    
                    visited.add((x, y))
                    
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                            n_word = c_word + board[nx][ny]

                            if trie.find_pref(n_word):
                                dfs.append((nx, ny, n_word, visited))
        
        return list(res)