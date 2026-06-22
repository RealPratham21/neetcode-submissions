class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[l] < nums[r]:
                r = mid
            
            else:
                l = mid
        
        return nums[l]