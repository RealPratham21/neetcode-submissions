class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = curr = nums[0]
        res = float('-inf')

        for i in nums[1:]:
            cands = (i, maxProd * i, minProd * i)

            maxProd = max(cands)
            minProd = min(cands)

            res = max(res, maxProd)
        
        return res