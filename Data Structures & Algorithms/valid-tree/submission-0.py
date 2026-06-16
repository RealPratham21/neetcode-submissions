class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()

        def all_present(curr):
            seen.add(curr)

            for node in graph[curr]:
                if node not in seen:
                    all_present(node)

        all_present(0)
        
        return len(seen) == n and len(edges) == n - 1