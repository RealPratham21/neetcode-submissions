class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def merge(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if self.rank[parentX] > self.rank[parentY]:
            self.parent[parentY] = parentX
        
        elif self.rank[parentX] < self.rank[parentY]:
            self.parent[parentX] = parentY

        
        else:
            self.parent[parentX] = parentY
            self.rank[parentY] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges:
            uf.merge(u, v)

        grps = set()

        for i in range(n):
            grps.add(uf.find(i))
        
        return len(grps)