from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def dp(x, y):
            if (x, y) == (m - 1, n - 1):
                return 1
            
            # res = 0

            if y + 1 < n:
                right = dp(x, y + 1)
            else:
                right = 0

            if x + 1 < m:
                down = dp(x + 1, y)
            
            else:
                down = 0
            
            return right + down
        
        return dp(0, 0)