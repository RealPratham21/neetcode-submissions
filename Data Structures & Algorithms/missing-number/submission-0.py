class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        n = len(nums)

        for i in range(n):
            res += i - nums[i]

        return res