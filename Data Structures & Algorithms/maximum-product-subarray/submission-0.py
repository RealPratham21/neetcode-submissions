class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')

        curr = 1

        for i in nums:
            extend = curr * i
            new = i

            curr = max(extend, new)

            res = max(res, curr)
        
        return res