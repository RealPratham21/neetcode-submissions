from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(step):
            if step > n:
                return 0
            
            if step == n:
                return 1
            
            res = 0

            res += dp(step + 1)

            res += dp(step + 2)

            return res
        
        return dp(0)