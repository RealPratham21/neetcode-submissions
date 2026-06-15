from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(pos):
            if pos >= n:
                return 0
            
            rob = dp(pos + 2) + nums[pos]

            skip = dp(pos + 1)

            return max(rob, skip)
        
        return dp(0)