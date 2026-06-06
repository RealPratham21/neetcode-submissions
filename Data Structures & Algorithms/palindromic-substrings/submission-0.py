class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        l = 0

        for r in range(n):
            sub = s[l:r+1]

            while l < r and sub != sub[::-1]:
                l += 1
            
            res += (r - l + 1)
        
        return res