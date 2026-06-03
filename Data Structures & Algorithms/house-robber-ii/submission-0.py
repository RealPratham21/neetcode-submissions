class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dp(pos, first):
            if pos >= n:
                return 0

            if first != -1 and (pos + 1) % n == first:
                return 0
            
            rob = dp(pos + 2, first if first != -1 else pos) + nums[pos]

            skip = dp(pos + 1, first)

            return max(rob, skip)
        
        return dp(0, -1)