class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        curr_chars = set()
        res = 0

        for r in range(n):
            while l < r and s[r] in curr_chars:
                curr_chars.remove(s[l])
                l += 1
            
            curr_chars.add(s[r])
            
            res = max(res, r - l + 1)
        
        return res