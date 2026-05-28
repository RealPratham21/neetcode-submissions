class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []

        m, n = len(heights), len(heights[0])

        for i in range(n):
            pacific.append((0, i))
        
        for i in range(m):
            pacific.append((i, 0))
        
        atlantic = []

        for i in range(n):
            atlantic.append((m - 1, i))
        
        for i in range(m):
            atlantic.append((i, n - 1))

        pacific_visited = set()

        while pacific:
            x, y = pacific.pop()

            pacific_visited.add((x, y))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in pacific_visited:
                    pacific.append((nx, ny))
        
        atlantic_visited = set()

        while atlantic:
            x, y = atlantic.pop()

            atlantic_visited.add((x, y))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in atlantic_visited:
                    atlantic.append((nx, ny))

        res = []

        atlantic_visited = list(atlantic_visited)

        for x, y in atlantic_visited:
            if (x, y) in pacific_visited:
                res.append((x, y))
        
        return res