class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def expand(l, r):
            cnt = 0

            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            
            return cnt
        
        res = 0

        for i in range(n):
            res += expand(i, i)
            res += expand(i, i + 1)
        
        return res