class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def find_combs(pos, curr, csum):
            if pos >= n or csum > target:
                return
            
            if csum == target:
                res.append(curr)
                return
            
            find_combs(pos, curr + [nums[pos]], csum + nums[pos])