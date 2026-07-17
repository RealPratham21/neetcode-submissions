class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0

        coins.sort(reverse=True)

        for i in coins:
            if (amount // i) > 0:
                res += amount // i
                amount %= i

        return res if amount == 0 else -1