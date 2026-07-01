class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        res = 0
        
        def find(x, y):
            bfs = deque([(x, y)])

            while bfs:
                x, y = bfs.popleft()

                seen.add((x, y))
                

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and grid[nx][ny] == '1':
                        bfs.append((nx, ny))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    res += 1
                
                    find(i, j)
        
        return res