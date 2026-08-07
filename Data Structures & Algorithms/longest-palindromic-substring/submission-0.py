class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr = s[i:j+1]

                if curr == curr[::-1] and len(res) < len(curr):
                    res = curr
            
        return res