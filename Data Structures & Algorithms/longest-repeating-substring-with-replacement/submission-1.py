class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        cnt = Counter()
        maxFreq = 0
        l = 0

        res = 0

        for r in range(n):
            cnt[s[r]] += 1

            maxFreq = max(maxFreq, cnt[s[r]])

            while (r - l + 1) - maxFreq > k:
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res