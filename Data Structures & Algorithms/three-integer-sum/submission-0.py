class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        n = len(nums)

        l, r = 0, n - 1
        res = set()


        for l in range(n):
            numMap = defaultdict(int)

            for r in range(l + 1, n):
                target = -(nums[l] + nums[r])

                if target in numMap:
                    res.add(tuple(sorted([nums[l], target, nums[r]])))
                
                numMap[nums[r]] += 1
        
        return list(res)