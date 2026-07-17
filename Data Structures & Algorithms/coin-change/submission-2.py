class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)

        def dp(pos, remain):
            if remain == 0:
                return 0
            
            if pos >= n:
                return float('inf')
            
            min_moves = float('inf')

            if remain >= coins[pos]:
                take = dp(pos, remain - coins[pos]) + 1
                # take_stay = dp(pos, remain % coins[pos]) + (remain // coins[pos])
            else:
                take = float('inf')

            skip = dp(pos + 1, remain)

            return min(take, skip)
        
        res = dp(0, amount)

        return res if res != float('inf') else -1