class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return l + 1, r - 1
        
        n = len(s)
        res = ''
        
        for i in range(n):
            odd_l, odd_r = expand(i, i)

            if odd_r - odd_l + 1 > len(res):
                res = s[odd_l:odd_r + 1]
            
            even_l, even_r = expand(i, i + 1)

            if even_r - even_l + 1 > len(res):
                res = s[even_l:even_r + 1]
        
        return res