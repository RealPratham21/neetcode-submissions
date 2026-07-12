class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)
        
        def find_combs(pos, curr, csum):
            if pos >= n or csum > target:
                return
            
            if csum == target:
                res.add(tuple(curr))
                return
            
            find_combs(pos, curr + [nums[pos]], csum + nums[pos])
            find_combs(pos + 1, curr + [nums[pos]], csum + nums[pos])
            find_combs(pos + 1, curr, csum)
        
        find_combs(0, [], 0)

        final_res = []

        for i in res:
            final_res.append(list(i))
        
        return final_res