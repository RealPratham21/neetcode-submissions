class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, prices[j] - prices[i])
        
        return res